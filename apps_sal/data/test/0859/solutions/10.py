import sys
import math
import os


data1 = input()
data2 = input()

a, b = 0, 0
c, d = 0, 0
vprs = 0

for i in range(len(data1)):
    if data1[i] == '+':
        a += 1
    else:
        b += 1


for i in range(len(data2)):
    if data2[i] == '+':
        c += 1
    elif data2[i] == '-':
        d += 1
    else:
        vprs += 1

if vprs == 0:
    if a == c and b == d:
        print("%.9f" % 1)
    else:
        print("%.9f" % 0)
else:
    if c > a or d > b:
        print("%.9f" % 0)
    else:
        deltaM = a - c
        deltaP = b - d
        total = 2**vprs
        fak1 = 1
        fak2 = 1
        fak3 = 1
        for i in range(1, vprs + 1):
            fak1 *= i
        for i in range(1, deltaM + 1):
            fak2 *= i
        for i in range(1, deltaP + 1):
            fak3 *= i
        ans = (fak1 / (fak2 * fak3)) / total
        print("%.9f" % ans)
