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
    (n, k, c) = LI()
    s = S()
    l = set()
    i = 0
    while i < n:
        if s[i] == 'x':
            i += 1
        else:
            l.add(i + 1)
            i += c + 1
    if len(l) > k:
        return ''
    r = set()
    i = n - 1
    while i >= 0:
        if s[i] == 'x':
            i -= 1
        else:
            r.add(i + 1)
            i -= c + 1
    return JA(sorted(l & r), '\n')


print(main())
