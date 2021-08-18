import itertools
from scipy.sparse.csgraph import floyd_warshall

N, M = map(int, input().split())

dist = []
for i in range(N):
    tmp = []
    for _ in range(N):
        tmp.append(float('inf'))
    dist.append(tmp)
    dist[i][i] = 0

a = []
b = []
c = []
for _ in range(M):
    x = list(map(int, input().split()))
    a.append(x[0] - 1)
    b.append(x[1] - 1)
    c.append(x[2])
    dist[a[-1]][b[-1]] = x[2]
    dist[b[-1]][a[-1]] = x[2]

dist = floyd_warshall(dist)
dist = dist.astype(int).tolist()

res = 0
for i in range(M):
    if c[i] > dist[a[i]][b[i]]:
        res += 1

print(res)
