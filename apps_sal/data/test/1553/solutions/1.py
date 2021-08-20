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
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
eps = 1.0 / 10 ** 10
mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI():
    return tuple(map(int, sys.stdin.readline().split()))


def LLI():
    return [tuple(map(int, l.split())) for l in sys.stdin]


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
    (n, h) = LI()
    a = LI()

    def f(i):
        if i > n:
            return False
        b = sorted(a[:i])
        t = None
        if i % 2 == 1:
            t = sum(b[::2])
        else:
            t = sum(b[1::2])
        return t <= h
    r = bs(f, 0, n + 1)
    return r - 1


print(main())
