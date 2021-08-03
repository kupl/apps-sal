# -*- coding: utf-8 -*-
from scipy.sparse.csgraph import floyd_warshall

N, M, L = map(int, input().split())

d = [[0 for i in range(N)] for j in range(N)]
for i in range(M):
    x, y, z = map(int, input().split())
    d[x - 1][y - 1] = z
    d[y - 1][x - 1] = z
for i in range(N):
    d[i][i] = 0

d = floyd_warshall(d, directed=False)
LN = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    for j in range(N):
        if d[i][j] <= L:
            LN[i][j] = 1
            LN[j][i] = 1

LN = floyd_warshall(LN, directed=False)
s = []
t = []
Q = int(input())
for i in range(Q):
    s1, t1 = map(int, input().split())
    s.append(s1)
    t.append(t1)
for i in range(Q):
    if LN[s[i] - 1][t[i] - 1] == float("inf"):
        print(-1)
    else:
        print(int(LN[s[i] - 1][t[i] - 1] - 1))
