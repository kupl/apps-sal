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
#from operator import itemgetter
#from heapq import heappush, heappop
import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
#from scipy.sparse import csr_matrix
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
import sys

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin


def ni(): return int(ns())
def nf(): return float(ns())
def na(): return list(map(int, stdin.readline().split()))
def nb(): return list(map(float, stdin.readline().split()))
def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


N, X, Y = na()
g = [[0] * N for _ in range(N)]
for i in range(N - 1):
    g[i][i + 1] = 1
    g[i + 1][i] = 1

g[X - 1][Y - 1] = 1
g[Y - 1][X - 1] = 1
g = np.array(g)
d = shortest_path(g)
ct = [0] * N
for i in range(N):
    for j in range(i, N):
        ct[int(d[i][j])] += 1
for i in range(1, N):
    print((ct[i]))
