import math
import sys
import re
import itertools
import pprint
import collections
import copy
rs, ri, rai, raf = input, lambda: int(input()), lambda: list(map(int, input().split())), lambda: list(map(float, input().split()))

n = ri()
x0, y0 = rai()

rays = [
    [[], lambda x, y: x == x0 and y > y0],
    [[], lambda x, y: x == x0 and y < y0],
    [[], lambda x, y: y == y0 and x > x0],
    [[], lambda x, y: y == y0 and x < x0],
    [[], lambda x, y: x - x0 == y - y0 and x > x0],
    [[], lambda x, y: x - x0 == y - y0 and x < x0],
    [[], lambda x, y: x - x0 == -(y - y0) and x > x0],
    [[], lambda x, y: x - x0 == -(y - y0) and x < x0],
]

for i in range(n):
    t = input().split()
    x, y = int(t[1]), int(t[2])
    t = (t[0], x, y)
    for k, v in rays:
        if v(x, y):
            k.append(t)


def dist(a): return abs(x0 - a[1]) + abs(y0 - a[2])


flag = False
for i, (k, v) in enumerate(rays):
    k.sort(key=dist)
    if len(k) > 0 and i > 3 and k[0][0] in "BQ":
        flag = True
        break
    if len(k) > 0 and i <= 3 and k[0][0] in "RQ":
        flag = True
        break

print("YES" if flag else "NO")
