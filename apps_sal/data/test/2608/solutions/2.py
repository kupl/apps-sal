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
import random
import time
import copy
import functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
mod = 10**9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    q = I()
    rr = []

    def f(a, b, c, d):
        if a > c or b > d:
            return (0, 0)
        sa = c - a + 1
        sb = d - b + 1
        g = h = (sa * sb) // 2
        if (sa * sb) % 2 == 1:
            g += 1

        if (a + b) % 2 == 0:
            return (g, h)
        return (h, g)

    def fa(a):
        return f(a[0], a[1], a[2], a[3])

    for _ in range(q):
        n, m = LI()
        wa = LI()
        ba = LI()
        wc, bc = f(1, 1, n, m)
        w1, b1 = fa(wa)
        w2, b2 = fa(ba)
        w3, b3 = f(max(wa[0], ba[0]), max(wa[1], ba[1]), min(wa[2], ba[2]), min(wa[3], ba[3]))

        wc += b1
        bc -= b1
        wc -= w2
        bc += w2
        wc -= b3
        bc += b3
        rr.append('{} {}'.format(wc, bc))

    return "\n".join(map(str, rr))


print(main())
