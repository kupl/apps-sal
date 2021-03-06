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
from operator import itemgetter
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
mod = 10 ** 9 + 7
stdin = sys.stdin


def ni():
    return int(ns())


def na():
    return list(map(int, stdin.readline().split()))


def ns():
    return stdin.readline().rstrip()


def cmb(n, r, mod):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 10 ** 9 + 7
N = 10 ** 4
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]
for i in range(2, N + 1):
    g1.append(g1[-1] * i % mod)
    inverse.append(-inverse[mod % i] * (mod // i) % mod)
    g2.append(g2[-1] * inverse[-1] % mod)
(N, K) = na()
for i in range(K):
    print(cmb(K - 1, i, mod) * cmb(N - K + 1, N - K - i, mod) % mod)
