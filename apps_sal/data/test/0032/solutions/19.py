# -*- coding: utf-8 -*-
# @Author: q7199
# @Date:   2016-12-30 22:25:59
# @Last Modified by:   q7199
# @Last Modified time: 2016-12-30 22:30:38

n = input()
flag = True
now = [0, 0]
for i in range(int(n)):
    step, way = input().split()
    if now[0] == 0 and way != "South":
        flag = False
        break
    if now[0] == 20000 and way != "North":
        flag = False
        break
    if way == "South":
        now[0] += int(step)
    elif way == "North":
        now[0] -= int(step)
    elif way == "West":
        now[1] += int(step)
    elif way == "East":
        now[1] -= int(step)
    if now[0] > 20000 or now[0] < 0:
        # print("NO")
        flag = False
        break
if flag and now[0] == 0:
    print("YES")
else:
    print("NO")
