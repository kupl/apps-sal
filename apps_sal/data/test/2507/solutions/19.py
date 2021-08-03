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


def bs(f, mi, ma):
    mm = -1
    while ma > mi:
        mm = (ma + mi) // 2
        if f(mm):
            mi = mm + 1
        else:
            ma = mm
    if f(mm):
        return mm + 1
    return mm


def main():
    n, k = LI()
    a = sorted(LI())
    b = sorted(LI(), reverse=True)
    if sum(a) <= k:
        return 0

    def f(i):
        t = 0
        for ai, bi in zip(a, b):
            u = i // bi
            if ai > u:
                t += ai - u
        return t > k

    r = bs(f, 0, 10**12)

    return r


print(main())
