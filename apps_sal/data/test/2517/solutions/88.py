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
import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin


def ni(): return int(ns())
def nf(): return float(ns())
def na(): return list(map(int, stdin.readline().split()))
def nb(): return list(map(float, stdin.readline().split()))
def ns(): return stdin.readline().rstrip()


N, M, R = na()
r = na()
g = [[0] * N for _ in range(N)]
for i in range(M):
    a, b, c = na()
    a -= 1
    b -= 1
    g[a][b] = c
    g[b][a] = c

g = np.array(g)
d = shortest_path(g)

R = len(r)
ans = inf
for x in itertools.permutations(r):
    tmp = 0
    for i in range(R - 1):
        tmp += d[x[i] - 1][x[i + 1] - 1]
    ans = min(ans, tmp)
print((int(ans)))
