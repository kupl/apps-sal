#!/usr/bin/env python3

from fractions import Fraction
from math import sqrt


def gety(a, b, c, x):
    return -Fraction(a * x + c, b)


def getx(a, b, c, y):
    return -Fraction(b * y + c, a)


def ds(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


a, b, c = list(map(int, input().split()))
x1, y1, x2, y2 = list(map(int, input().split()))

silly_dist = abs(x1 - x2) + abs(y1 - y2)
if a == 0 or b == 0:
    print(silly_dist)
    return

dq = silly_dist

mx = x1
my = gety(a, b, c, mx)
ny = y1
nx = getx(a, b, c, ny)

kx = x2
ky = gety(a, b, c, kx)
ty = y2
tx = getx(a, b, c, ty)

dq1 = ds(mx, my, kx, ky) + ds(mx, my, x1, y1) + ds(kx, ky, x2, y2)
dq2 = ds(nx, ny, kx, ky) + ds(nx, ny, x1, y1) + ds(kx, ky, x2, y2)
dq3 = ds(mx, my, tx, ty) + ds(mx, my, x1, y1) + ds(tx, ty, x2, y2)
dq4 = ds(nx, ny, tx, ty) + ds(nx, ny, x1, y1) + ds(tx, ty, x2, y2)

#print([dq, dq1, dq2, dq3, dq4])
dqmin = min([dq, dq1, dq2, dq3, dq4])
print(dqmin)
