#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

"""
"""

from collections import Counter
from itertools import accumulate
from itertools import chain

x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
xx = x2 - x1
yy = y2 - y1
n = int(input())
s = list(input())

letterdict = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
pxli = list(chain(iter([0]), accumulate([letterdict[ll][0] for ll in s])))
pyli = list(chain(iter([0]), accumulate([letterdict[ll][1] for ll in s])))

dx = pxli[-1]
dy = pyli[-1]


def isreachable(x, y, d, divmod=divmod):
    cyc, m = divmod(d, n)
    ddx = dx * cyc + pxli[m]
    ddy = dy * cyc + pyli[m]
    return abs(x - ddx) + abs(y - ddy) <= d


if not isreachable(xx, yy, 10**17):
    print(-1)
    return

db = 10**17
ds = 0
while db - ds > 1:
    dm = (db + ds) // 2
    if isreachable(xx, yy, dm):
        db = dm
    else:
        ds = dm

if isreachable(xx, yy, ds):
    print(ds)
else:
    print(ds + 1)
