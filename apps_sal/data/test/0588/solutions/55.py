# 無理やり0.1度ずつ行先を回す。

import math
import numpy as np

n = int(input())

eng_list = []

for _ in range(n):
    a = np.array(list(map(int, input().split())))
    eng_list.append(a)

# 角度
angles = []

for i in range(n):
    cos = (np.dot(eng_list[i], np.array([0, 1]))/(np.linalg.norm(eng_list[i])))
    angle = math.degrees(math.acos(cos))
    if eng_list[i][0] < 0:
        angle = 360 - angle
    angles.append(angle)


def hantei(a, b):
    coss = np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))
    if coss > 1:
        coss = 1.0
    elif coss < -1:
        coss = -1.0
    angg = math.degrees(math.acos(coss))
    if angg < 90.0001:
        return True
    else:
        return False


def distance(a):
    dis = np.linalg.norm(a)
    return dis

pitch = 1 # 角度
dist = []

for ikisaki in np.arange(0, 360, pitch):
    dist_location = np.array([0, 0])
    for j in eng_list:
        i = np.array([math.cos(math.radians(ikisaki)), math.sin(math.radians(ikisaki))])
        if hantei(i, j):
            dist_location = dist_location + j
    dist.append(distance(dist_location))

print((max(dist)))

