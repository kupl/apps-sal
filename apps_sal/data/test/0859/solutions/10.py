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
        # print(1.000000000)
    else:
       # print(0.000000000)
        print("%.9f" % 0)
else:
    if c > a or d > b:
        # print(0.000000000)
        print("%.9f" % 0)
    else:
        deltaM = a - c
        deltaP = b - d
        total = 2**vprs
        fak1 = 1
        fak2 = 1
        fak3 = 1
      #  print(deltaM,deltaP)
        for i in range(1, vprs + 1):
            fak1 *= i
        for i in range(1, deltaM + 1):
            fak2 *= i
        for i in range(1, deltaP + 1):
            fak3 *= i
        # print(total)
        # print((fak1/fak2)/total)
        ans = (fak1 / (fak2 * fak3)) / total
       # print(fak1,fak2,fak3)
        print("%.9f" % ans)
