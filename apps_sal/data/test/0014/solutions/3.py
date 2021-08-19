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
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
eps = 1.0 / 10 ** 15
mod = 10 ** 9 + 7


def LI():
    return [int(x) for x in sys.stdin.readline().split()]


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


def main():
    (n, k) = LI()
    a = LI()
    r = a[:]
    s = []
    m = 1
    for c in a:
        if c == m:
            m += 1
            t = len(s)
            for i in range(t - 1, -1, -1):
                if s[i] == m:
                    m += 1
                    t = i
                else:
                    break
            if t != len(s):
                s = s[:t]
        else:
            s.append(c)
    for i in range(len(s) - 1):
        if s[i] < s[i + 1]:
            return -1
    for i in range(len(s) - 1, -1, -1):
        c = s[i]
        r += list(range(c - 1, m - 1, -1))
        m = c + 1
    r += list(range(n, m - 1, -1))
    return ' '.join(map(str, r))


print(main())
