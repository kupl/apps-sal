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


N = ni()
A = na()
b = [0] * N
c = [0] * N
b[0] = A[0]
c[-1] = A[-1]
for i in range(N - 1):
    b[i + 1] = math.gcd(b[i], A[i + 1])
    c[-(i + 2)] = math.gcd(c[-(i + 1)], A[-(i + 2)])

ans = 1
ans = max(c[1], ans)
ans = max(b[-2], ans)
for i in range(1, N - 1):
    ans = max(math.gcd(b[i - 1], c[i + 1]), ans)
print(ans)
