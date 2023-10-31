import time
import almath
import math
import numpy as np
from naoqi import ALProxy

PORT=9559
IP="192.168.12.110"
motion = ALProxy("ALMotion",IP,PORT)
post = ALProxy("ALRobotPosture",IP,PORT)
post.goToPosture("Stand",0.5)
motion.moveTo(0.5, 0, 0)
time.sleep(1.0)
names = ["HeadYaw","HeadPitch"]
angleLists0 = [0 * almath.TO_RAD, 20 * almath.TO_RAD]
timeLists = [0.5,0.5]
motion.setStiffnesses('HeadPitch', 1.0)
motion.setStiffnesses('HeadYaw', 1.0)
motion.angleInterpolation(names, angleLists0, timeLists, True)
post.goToPosture("Crouch",0.5)
