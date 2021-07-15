import math
import re


def ria():
    return [int(i) for i in input().split()]


def ri():
    return int(input())


def rfa():
    return [float(i) for i in input().split()]


eps = 1e-9


def is_equal(a, b):
    return abs(a - b) <= eps


def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)


xq, yq = ria()
xp, yp = ria()
ar = [(xp + 1, yp+1), (xp - 1, yp-1), (xp-1, yp + 1), (xp+1, yp - 1)]

if xp == xq:
    print(2 * 2 + (abs(yp - yq) + 1) * 2)
    return
if yp == yq:
    print(2 * 2 + (abs(xp - xq) + 1) * 2)
    return
mni = 1e+9

for i in ar:
    x1, y1 = i
    mxx, mxy, mnx, mny = max(x1, xq), max(y1, yq), min(x1, xq), min(y1, yq)
    #print(mxx,mxy,mnx,mny)
    if mxx > xp and mxy > yp and mnx < xp and mny < yp:
        mni = min(mni, (mxx - mnx) * 2 + (mxy - mny) * 2)
print(mni)

