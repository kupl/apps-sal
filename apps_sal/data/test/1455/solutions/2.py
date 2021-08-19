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


def YESNO(ans, yes='YES', no='NO'):
    print([no, yes][ans])


def II():
    return int(input())


def MI():
    return list(map(int, input().split()))


def MIL():
    return list(MI())


def MIS():
    return input().split()


def main():
    N = II()
    M = math.ceil((N + 1) / 2)
    print(M)
    (x, y) = (1, 1)
    for i in range(1, N + 1):
        print(x, y)
        if i % 2 == 0:
            y += 1
        else:
            x += 1


def __starting_point():
    main()


__starting_point()
