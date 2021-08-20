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
    (h, w, k) = LI()
    (y1, x1, y2, x2) = LI_()
    ca = [S() for _ in range(h)]
    aa = [[-1 if c == '@' else inf for c in s] for s in ca]
    aa[y1][x1] = 0
    q = [(y1, x1)]
    v = collections.defaultdict(bool)
    t = 0
    while q:
        t += 1
        nq = []
        for (y, x) in q:
            for (dy, dx) in dd:
                for i in range(1, k + 1):
                    ty = y + dy * i
                    tx = x + dx * i
                    if ty < 0 or ty >= h or tx < 0 or (tx >= w) or (aa[ty][tx] < t):
                        break
                    if aa[ty][tx] == t:
                        continue
                    aa[ty][tx] = t
                    nq.append((ty, tx))
        q = nq
    if aa[y2][x2] == inf:
        return -1
    return aa[y2][x2]


print(main())
