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


def main():
    h, w = LI()
    a = [LI() for _ in range(h)]
    b = [LI() for _ in range(h)]
    m = 1 << (80 * 80 * 2 + 3)
    r = [[0] * w for _ in range(h)]
    c = abs(a[0][0] - b[0][0])
    r[0][0] |= (1 << (80 * 80 + 1)) << c
    r[0][0] |= (1 << (80 * 80 + 1)) >> c
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                continue
            c = abs(a[i][j] - b[i][j])
            t = 0
            if i > 0:
                t |= (r[i - 1][j] << c) % m
                t |= r[i - 1][j] >> c
            if j > 0:
                t |= (r[i][j - 1] << c) % m
                t |= r[i][j - 1] >> c
            r[i][j] = t

    c = r[-1][-1]
    t = 10000
    for i in range((80 * 80 * 2 + 3)):
        if (1 << i) & c > 0:
            k = abs(i - (80 * 80 + 1))
            if t > k:
                t = k

    return t


print(main())
