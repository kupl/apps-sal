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
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
mod = 10 ** 9 + 7


def LI():
    return list(map(int, input().split()))


def II():
    return int(input())


def LS():
    return input().split()


def S():
    return input()


def main():
    n = II()
    a = list([x - 1 for x in LI()])
    g = [-1] * n
    h = list(set(a))
    l = len(h)
    d = {}
    for i in range(l):
        hi = h[i]
        g[hi] = i
    for i in range(n):
        if g[i] == -1:
            g[i] = g[a[i]]
        elif g[i] != g[a[i]]:
            return -1
    print(l)
    print(' '.join([str(x + 1) for x in g]))
    return ' '.join([str(x + 1) for x in h])


print(main())
