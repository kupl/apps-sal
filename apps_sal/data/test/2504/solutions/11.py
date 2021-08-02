import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
import sys


def input():
    return sys.stdin.readline()[:-1]


n, m, l = map(int, input().split())
dist = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a - 1][b - 1] = c
    dist[b - 1][a - 1] = c

fw = floyd_warshall(csr_matrix(dist))

num = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if fw[i][j] <= l:
            num[i][j] = 1

ans = floyd_warshall(csr_matrix(num))

q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    if ans[s - 1][t - 1] > n:
        print(-1)
    else:
        print(int(ans[s - 1][t - 1]) - 1)
