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


def VI(): return list(map(int, input().split()))
def I(): return int(input())
def LIST(n, m=None): return [0] * n if m is None else [[0] * m for i in range(n)]
def ELIST(n): return [[] for i in range(n)]


def MI(n=None, m=None):
    if n is None:
        n, m = VI()
    arr = LIST(n)
    for i in range(n):
        arr[i] = VI()
    return arr


def MS(n=None, m=None):
    if n is None:
        n, m = VI()
    arr = LIST(n)
    for i in range(n):
        arr[i] = input()
    return arr


def MIT(n=None, m=None):
    if n is None:
        n, m = VI()
    a = MI(n, m)
    arr = LIST(m, n)
    for i, l in enumerate(a):
        for j, x in enumerate(l):
            arr[j][i] = x
    return arr


def run(na, nb, k, m, a, b):
    if a[k - 1] < b[nb - m]:
        print("YES")
    else:
        print("NO")


def main(info=0):
    na, nb = VI()
    k, m = VI()
    a = VI()
    b = VI()
    run(na, nb, k, m, a, b)


def __starting_point():
    main()


__starting_point()
