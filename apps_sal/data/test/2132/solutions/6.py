#!/usr/bin/env python3
from sys import stdin, stdout
from math import inf

def rint():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()

csp = 0
ov = 1

sign = []
ans = 0
spst = [inf]
ovst = [1]
n = int(input())
for i in range(n):
    sign = list(rint())
    if sign[0] == 1:
        csp = sign[1]
        while csp > spst[-1]:
            spst.pop()
            ans += 1
    if sign[0] == 2:
        while ovst[-1] == 0:
            ovst.pop()
            ans += 1
    if sign[0] == 3:
        if sign[1] >= csp:
            spst.append(sign[1])
        else:
            ans += 1
    if sign[0] == 4:
        ovst.append(1)
    if sign[0] == 5:
        spst.append(inf)
    if sign[0] == 6:
        ovst.append(0)
print(ans)

