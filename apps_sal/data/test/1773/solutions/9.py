import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import copy
from itertools import chain, dropwhile, permutations, combinations
from collections import defaultdict, deque

# Guide:
#   1. construct complex data types while reading (e.g. graph adj list)
#   2. avoid any non-necessary time/memory usage
#   3. avoid templates and write more from scratch
#   4. switch to "flat" implementations


def VI(): return list(map(int, input().split()))
def I(): return int(input())
def LIST(n, m=None): return [0] * n if m is None else [[0] * m for i in range(n)]
def ELIST(n): return [[] for i in range(n)]


def MI(n=None, m=None):  # input matrix of integers
    if n is None:
        n, m = VI()
    arr = LIST(n)
    for i in range(n):
        arr[i] = VI()
    return arr


def MS(n=None, m=None):  # input matrix of strings
    if n is None:
        n, m = VI()
    arr = LIST(n)
    for i in range(n):
        arr[i] = input()
    return arr


def MIT(n=None, m=None):  # input transposed matrix/array of integers
    if n is None:
        n, m = VI()
    a = MI(n, m)
    arr = LIST(m, n)
    for i, l in enumerate(a):
        for j, x in enumerate(l):
            arr[j][i] = x
    return arr


def run(n, x, l, r):
    s = 0
    curr = 1
    for i in range(n):
        skip = (l[i] - curr) // x
        s += r[i] - curr - skip * x + 1
        curr = r[i] + 1
    print(s)


def main(info=0):
    n = I()
    #x,a = MIT(n,2)

    m = MI(n, 2)

    p = sorted([tuple(x) for x in m if x[0] > 0])
    n = sorted([tuple(x) for x in m if x[0] < 0])[::-1]

    pn = len(p)
    nn = len(n)
    mn = min(pn, nn)

    def apples(arr, l):
        return sum(x[1] for x in arr[:l])

    if nn > pn:
        ans = apples(n, mn + 1) + apples(p, mn)
    elif pn > nn:
        ans = apples(n, mn) + apples(p, mn + 1)
    else:
        ans = apples(n, mn) + apples(p, mn)

    print(ans)


def __starting_point():
    main()


__starting_point()
