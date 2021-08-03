import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import copy
import functools
import time
import random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9 + 7
mod2 = 998244353
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def distance_p(a, b):
    return distance(a[0], a[1], b[0], b[1])


def distance3(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    ax = x2 - x1
    ay = y2 - y1
    bx = x3 - x1
    by = y3 - y1

    r = (ax * bx + ay * by) / (ax * ax + ay * ay)
    pt = (x1 + r * ax, y1 + r * ay, 0)
    return distance_p(pt, p3)


def gaisin(xy):
    a = xy[0][0]
    b = xy[0][1]
    c = xy[1][0]
    d = xy[1][1]
    e = xy[2][0]
    f = xy[2][1]

    t1 = (e - a) * (a**2 + b**2 - c**2 - d**2)
    t2 = (c - a) * (a**2 + b**2 - e**2 - f**2)
    t3 = 2 * (e - a) * (b - d) - 2 * (c - a) * (b - f)
    py = (t1 - t2) / t3
    if c - a != 0:
        px = (2 * (b - d) * py - a**2 - b**2 + c**2 + d**2) / (2 * (c - a))
    else:
        px = (2 * (b - f) * py - a**2 - b**2 + e**2 + f**2) / (2 * (e - a))
    return (px, py)


def main():
    n = I()
    xy = [LI() for _ in range(n)]

    if n == 2:
        return distance_p(xy[0], xy[1]) / 2

    r = inf
    for i in range(n):
        t1 = xy[i]
        for j in range(i + 1, n):
            t2 = xy[j]
            p = ((t1[0] + t2[0]) / 2, (t1[1] + t2[1]) / 2)
            tr = max(distance_p(p, xy[l]) for l in range(n))
            if r > tr:
                r = tr
            xf = t1[0] == t2[0]
            yf = t1[1] == t2[1]
            for k in range(j + 1, n):
                t3 = xy[k]
                if distance3(t1, t2, t3) < eps:
                    continue
                p = gaisin([t1, t2, t3])
                tr = max(distance_p(p, xy[l]) for l in range(n))
                if r > tr:
                    r = tr

    return r


print(main())
