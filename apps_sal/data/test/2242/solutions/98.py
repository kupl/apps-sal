# 解説AC
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
#import numpy as np
#from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
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


S = ns()
n = len(S)
T = [0] * (n + 1)
d = {0: 1}
for k in range(n - 1, -1, -1):
    tmp = (T[k + 1] + pow(10, n - k - 1, 2019) * int(S[k])) % 2019
    T[k] = tmp
    if tmp not in list(d.keys()):
        d[tmp] = 1
    else:
        d[tmp] += 1
ans = 0
for k, v in list(d.items()):
    ans += v * (v - 1) // 2
print(ans)
