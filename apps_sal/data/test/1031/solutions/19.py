import os
import sys
import math
import heapq
from decimal import *
from io import BytesIO, IOBase
from collections import defaultdict, deque


def r():
    return int(input())


def rm():
    return map(int, input().split())


def rl():
    return list(map(int, input().split()))


n = r()
a = rl()
w = sum(a)
h = -math.inf
d = math.inf
ptr = 0
for i, j in enumerate(a):
    ptr += (j - 1 if i % 2 == 0 else 1 - j)
    h = max(h, ptr)
    d = min(d, ptr)

b = [[' '] * w for i in range(h + abs(d) + 1)]
j = 0
incr = True
for i in range(n):
    H = a[i]
    while H != 0:
        if incr:
            b[h][j] = '/'
            j += 1
            h -= 1
        else:
            b[h][j] = '\\'
            j += 1
            h += 1
        H -= 1
    if incr:
        h += 1
    else:
        h -= 1
    incr = not incr
for i in b:
    print(*i, sep='')
