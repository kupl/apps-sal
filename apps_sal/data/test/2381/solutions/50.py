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
import resource
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
eps = 1.0 / 10 ** 10
mod = 10 ** 9 + 7
mod2 = 998244353
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI():
    return [list(map(int, l.split())) for l in sys.stdin.readlines()]


def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]


def LF():
    return [float(x) for x in sys.stdin.readline().split()]


def LS():
    return sys.stdin.readline().split()


def I():
    return int(sys.stdin.readline())


def F():
    return float(sys.stdin.readline())


def S():
    return input()


def pf(s):
    return print(s, flush=True)


def pe(s):
    return print(str(s), file=sys.stderr)


def JA(a, sep):
    return sep.join(map(str, a))


def JAA(a, s, t):
    return s.join((t.join(map(str, b)) for b in a))


def main():
    (n, k) = LI()
    a = sorted(LI())
    r = 1
    i = n - 1
    j = 0
    if k % 2 == 1:
        r = a[i]
        i -= 1
    mf = r < 0
    for _ in range(k // 2):
        t = a[i] * a[i - 1]
        u = a[j] * a[j + 1]
        if not mf and t >= u or (mf and t < u):
            r *= t
            r %= mod
            i -= 2
        else:
            r *= u
            r %= mod
            j += 2
    return r


print(main())
