# -*- coding: utf-8 -*-
from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect
import copy
import math
sys.setrecursionlimit(10**6)

# lis_of_lis = [[] for _ in range(N)]


def zz(): return list(map(int, sys.stdin.readline().split()))


def z(): return int(sys.stdin.readline())


def S(): return sys.stdin.readline()[:-1]


def C(line): return [sys.stdin.readline() for _ in range(line)]


H, W = zz()
C = []
for i in range(10):
    C.append(zz())
A = []
num_lis = [0]*10
for i in range(H):
    a = zz()
    for a_ in a:
        if (a_ == -1):
            continue
        num_lis[a_] += 1
    A.append(a)
# 1->1, 2->1, 3->1 にするためのコストを計算する
# cost = [0]*10
# for num in range(2, 10):
#     min_cost = C[num][1]
a = floyd_warshall(C)
ans = 0
for i, num in enumerate(num_lis):
    ans += a[i, 1]*num
print((int(ans)))

