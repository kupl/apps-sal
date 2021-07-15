import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy,bisect
from operator import itemgetter
#from heapq import heappush, heappop
import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
#from scipy.sparse import csr_matrix

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
nf = lambda: float(ns())
na = lambda: list(map(int, stdin.readline().split()))
nb = lambda: list(map(float, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

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
    for i in range(R-1):
        tmp += d[x[i] - 1][x[i+1] - 1]
    ans = min(ans, tmp)
print((int(ans)))





