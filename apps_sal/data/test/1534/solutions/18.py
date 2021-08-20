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
    s = [1 if c == 'a' else 0 for c in S()]
    l = len(s)
    a = [0] * l
    b = [0] * l
    if s[0] == 1:
        a[0] = 1
    else:
        b[0] = 1
    for i in range(1, l):
        if s[i] == 1:
            a[i] = a[i - 1] + 1
            b[i] = b[i - 1]
        else:
            a[i] = a[i - 1]
            b[i] = b[i - 1] + 1
    if b[-1] == 0:
        return l
    r = 0
    for i in range(0, l):
        if s[i] == 1:
            continue
        for j in range(i, l):
            if s[j] == 1:
                continue
            tr = a[i] + b[j] - b[i] + 1 + a[-1] - a[j]
            if r < tr:
                r = tr
    return r


print(main())
