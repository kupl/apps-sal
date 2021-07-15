#!/usr/bin/env python3
from math import hypot

EPS = 10 ** -8


def f(r):
    nonlocal n, xy
    cs = []
    for i in range(n):
        for j in range(i + 1, n):
            x0, y0 = xy[i]
            x1, y1 = xy[j]
            d = hypot(x1 - x0, y1 - y0)
            if r - d / 2 < EPS:
                continue
            h = (r ** 2 - (d / 2) ** 2) ** 0.5
            c = [(x0 + x1) / 2, (y0 + y1) / 2]
            cs.append([c[0] + h * (y0 - y1) / d, c[1] + h * (x1 - x0) / d])
            cs.append([c[0] - h * (y0 - y1) / d, c[1] - h * (x1 - x0) / d])
    for cx, cy in cs:
        if all(hypot(x - cx, y - cy) - r < EPS for x, y in xy):
            return True
    return False


n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
ok = 10 ** 9
ng = 0
while abs(ok - ng) > EPS:
    m = (ok + ng) / 2
    if f(m):
        ok = m
    else:
        ng = m
print(ok)

