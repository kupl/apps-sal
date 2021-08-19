import sys
import bisect
import math
import itertools
import string
import queue
import copy
import numpy as np
import scipy
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations
from heapq import heappop, heappush
from fractions import gcd
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
mod = 10 ** 9 + 7


def inp():
    return int(input())


def inpm():
    return list(map(int, input().split()))


def inpl():
    return list(map(int, input().split()))


def inpls():
    return list(input().split())


def inplm(n):
    return list((int(input()) for _ in range(n)))


def inplL(n):
    return [list(input()) for _ in range(n)]


def inplT(n):
    return [tuple(input()) for _ in range(n)]


def inpll(n):
    return [list(map(int, input().split())) for _ in range(n)]


def inplls(n):
    return sorted([list(map(int, input().split())) for _ in range(n)])


(N, X) = list(map(int, input().split()))
(a, p) = ([1], [1])
for i in range(N):
    a.append(a[i] * 2 + 3)
    p.append(p[i] * 2 + 1)


def f(N, X):
    if N == 0:
        return 0 if X <= 0 else 1
    elif X <= 1 + a[N - 1]:
        return f(N - 1, X - 1)
    else:
        return p[N - 1] + 1 + f(N - 1, X - 2 - a[N - 1])


print(f(N, X))
