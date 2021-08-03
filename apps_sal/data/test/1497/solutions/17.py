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


def main(info=0):
    n = I()
    a = MS(n)
    d = defaultdict(int)
    for x in a:
        d[x] += 1
    print(max(d.values()))


def __starting_point():
    main()


__starting_point()
