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


def run(n, a):
    for i in range(n + 1):
        if a[0] == 0:
            if sum([i == a[i] for i in range(n)]) == n:
                print("Yes")
            else:
                print("No")
            return
        for j in range(n):
            if j % 2 == 0:
                a[j] = (a[j] + 1) % n
            else:
                a[j] = (a[j] - 1) % n


def main(info=0):
    n = I()
    a = VI()

    run(n, a)


def __starting_point():
    main()


__starting_point()
