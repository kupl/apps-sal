# ----------------
# ここから
# ----------------

import sys
from io import StringIO
import unittest


def yn(b):
    print(("Yes" if b == 1 else "No"))
    return


def resolve():
    readline = sys.stdin.readline

    h, w, m = list(map(int, readline().rstrip().split()))
    cntH = [0] * h
    cntW = [0] * w

    ys = [0] * m
    xs = [0] * m

    for i in range(m):
        y, x = list(map(int, readline().rstrip().split()))
        y -= 1
        x -= 1
        cntH[y] += 1
        cntW[x] += 1
        ys[i] = y
        xs[i] = x
    maxX = max(cntW)
    maxY = max(cntH)
    cntMaxX = cntW.count(maxX)
    cntMaxY = cntH.count(maxY)
    cntMax = cntMaxX * cntMaxY

    for i in range(m):
        y = ys[i]
        x = xs[i]
        maxPtn = False
        if cntH[y] == maxY and cntW[x] == maxX:
            cntMax -= 1
    if cntMax > 0:
        print((maxX + maxY))
    else:
        print((maxX + maxY - 1))
    return


if 'doTest' not in globals():
    resolve()
    return

# ----------------
# ここまで
# ----------------
