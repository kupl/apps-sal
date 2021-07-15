#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

"""
"""

from collections import Counter

x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
xx = x2-x1
yy = y2-y1
n = int(input())
s = list(input())


pxli = [0]
pyli = [0]
tmpx = 0
tmpy = 0
for ll in s:
    if ll == 'U':
        tmpy += 1
    if ll == 'D':
        tmpy -= 1
    elif ll == 'R':
        tmpx += 1
    elif ll == 'L':
        tmpx -= 1
    pxli.append(tmpx)
    pyli.append(tmpy)

dx = pxli[-1]
dy = pyli[-1]


def isreachable(x, y, d, divmod=divmod):
    cyc, m = divmod(d, n)
    ddx = dx*cyc + pxli[m]
    ddy = dy*cyc + pyli[m]
    return abs(x-ddx)+abs(y-ddy) <= d


if not isreachable(xx, yy, 10**17):
    print(-1)
    return

db = 10**17
ds = 0
while db-ds > 1:
    dm = (db+ds)//2
    if isreachable(xx, yy, dm):
        db = dm
    else:
        ds = dm

if isreachable(xx, yy, ds):
    print(ds)
else:
    print(ds+1)


