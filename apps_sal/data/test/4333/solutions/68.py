# -*- coding:utf-8 -*-
x1, y1, x2, y2 = list(map(int, input().split()))

xdiff = x2 - x1
ydiff = y2 - y1

x3 = x2 - ydiff
y3 = y2 + xdiff

x4 = x3 - xdiff
y4 = y3 - ydiff

print((str(x3) + " " + str(y3) + " " + str(x4) + " " + str(y4)))
