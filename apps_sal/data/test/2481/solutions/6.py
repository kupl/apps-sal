import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy,bisect
from operator import itemgetter
from heapq import heappush, heappop
import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
nf = lambda: float(ns())
na = lambda: list(map(int, stdin.readline().split()))
nb = lambda: list(map(float, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces


H, W = na()
c = [na() for _ in range(10)]
A = [na() for _ in range(H)]
adj = [[] for _ in range(10)]

c = np.array(c)
d = shortest_path(c)
ans = 0
for y in range(H):
    for x in range(W):
        if A[y][x] != -1:
            #print(ans)
            ans += d[A[y][x]][1]
print((int(ans)))


