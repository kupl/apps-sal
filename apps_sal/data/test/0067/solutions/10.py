
import sys
import math

import array
import bisect
import collections
from collections import Counter, defaultdict
import fractions
import heapq
import re

sys.setrecursionlimit(1000000)


def array2d(dim1, dim2, init=None):
    return [[init for _ in range(dim2)] for _ in range(dim1)]


def argsort(l, reverse=False):
    return sorted(list(range(len(l))), key=lambda i: l[i], reverse=reverse)


def argmin(l):
    return l.index(min(l))


def YESNO(ans, yes="YES", no="NO"):
    print([no, yes][ans])


def II(): return int(input())
def MI(): return list(map(int, input().split()))
def MIL(): return list(MI())
def MIS(): return input().split()


def main():
    x, y, z = MI()
    u = x - y + z
    d = x - y - z
    if u > 0 and d > 0:
        return "+"
    if u < 0 and d < 0:
        return "-"
    if u == 0 and d == 0:
        return "0"
    return "?"


def __starting_point():
    print(main())


__starting_point()
