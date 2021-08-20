from math import ceil, floor, factorial, gcd, sqrt, log2, cos, sin, tan, acos, asin, atan, degrees, radians, pi, inf, comb
from itertools import accumulate, groupby, permutations, combinations, product, combinations_with_replacement
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
from operator import itemgetter
from heapq import heapify, heappop, heappush
from queue import Queue, LifoQueue, PriorityQueue
from copy import deepcopy
from time import time
from functools import reduce
import string
import sys
sys.setrecursionlimit(10 ** 7)


def input():
    return sys.stdin.readline().strip()


def INT():
    return int(input())


def MAP():
    return map(int, input().split())


def LIST():
    return list(MAP())


def bfs():
    dist = [-1] * n
    que = deque([0])
    dist[0] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in g[v]:
            if dist[w[0]] > -1:
                continue
            dist[w[0]] = d + w[1]
            que.append(w[0])
    return dist


n = INT()
g = [[] for i in range(n)]
for i in range(n - 1):
    (x, y, z) = MAP()
    g[x - 1].append([y - 1, z])
    g[y - 1].append([x - 1, z])
for k in bfs():
    print(0 if k % 2 == 0 else 1)
