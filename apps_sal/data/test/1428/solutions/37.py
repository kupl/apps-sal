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
import bisect
from operator import itemgetter
from heapq import heappush, heappop
import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
mod = 10 ** 9 + 7
stdin = sys.stdin


def ni():
    return int(ns())


def nf():
    return float(ns())


def na():
    return list(map(int, stdin.readline().split()))


def nb():
    return list(map(float, stdin.readline().split()))


def ns():
    return stdin.readline().rstrip()


(N, C) = na()
D = [na() for _ in range(C)]
c = [na() for _ in range(N)]
z = {}
o = {}
t = {}
for i in range(1, N + 1):
    for j in range(1, N + 1):
        q = (i + j) % 3
        now = c[i - 1][j - 1] - 1
        if q == 0:
            if now not in list(z.keys()):
                z[now] = 1
            else:
                z[now] += 1
        if q == 1:
            if now not in list(o.keys()):
                o[now] = 1
            else:
                o[now] += 1
        if q == 2:
            if now not in list(t.keys()):
                t[now] = 1
            else:
                t[now] += 1
ans = inf
for (i, j, l) in itertools.permutations(list(range(C)), 3):
    tmp = 0
    for (k, v) in list(z.items()):
        tmp += v * D[k][i]
    for (k, v) in list(o.items()):
        tmp += v * D[k][j]
    for (k, v) in list(t.items()):
        tmp += v * D[k][l]
    ans = min(tmp, ans)
print(ans)
