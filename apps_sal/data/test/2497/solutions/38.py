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

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353
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


def main():
    n = I()
    aa = [LS() for _ in range(n)]
    xi = collections.defaultdict(lambda: inf)
    xa = collections.defaultdict(lambda: -inf)
    yi = collections.defaultdict(lambda: inf)
    ya = collections.defaultdict(lambda: -inf)
    km = 0
    for x, y, d in aa:
        x = int(x)
        y = int(y)
        if km < abs(x):
            km = abs(x)
        if km < abs(y):
            km = abs(y)
        if xi[d] > x:
            xi[d] = x
        if xa[d] < x:
            xa[d] = x
        if yi[d] > y:
            yi[d] = y
        if ya[d] < y:
            ya[d] = y

    ts = set([0])

    for d in [xi, xa, yi, ya]:
        ks = list(d.keys())
        for k in ks:
            for e in ks:
                ts.add(abs(d[k] - d[e]))
                ts.add(abs(d[k] - d[e]) / 2)

    def f(i):
        xxi = inf
        xxa = -inf
        yyi = inf
        yya = -inf
        for d, x in xi.items():
            if d == 'L':
                x -= i
            elif d == 'R':
                x += i
            if xxi > x:
                xxi = x
        for d, x in xa.items():
            if d == 'L':
                x -= i
            elif d == 'R':
                x += i
            if xxa < x:
                xxa = x
        for d, y in yi.items():
            if d == 'D':
                y -= i
            elif d == 'U':
                y += i
            if yyi > y:
                yyi = y
        for d, y in ya.items():
            if d == 'D':
                y -= i
            elif d == 'U':
                y += i
            if yya < y:
                yya = y

        return (xxa - xxi) * (yya - yyi)

    r = f(0)
    for i in ts:
        t = f(i)
        if r > t:
            r = t

    return '{:0.3f}'.format(r)


print(main())
