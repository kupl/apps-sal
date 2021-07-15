# -*- coding: utf-8 -*-

N = int(input())

XY = []
for n in range(N):
    (x, y) = (int(i) for i in input().split())
    XY.append([x, y])

plus = []
minus = []
for [x, y] in XY:
    plus.append(x + y)
    minus.append(x - y)

print((max(max(plus)- min(plus), max(minus) - min(minus))))

