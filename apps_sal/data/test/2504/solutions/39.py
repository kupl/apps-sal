import sys
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

n, m, l = map(int, input().split())

d = [[sys.maxsize] * (n) for _ in range(n)]
e = [[sys.maxsize] * (n) for _ in range(n)]
for i in range(n):
    d[i][i] = 0
    e[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    d[a - 1][b - 1] = c
    d[b - 1][a - 1] = c

d = floyd_warshall(csr_matrix(d))
for i in range(n):
    for j in range(n):
        if d[i][j] <= l:
            e[i][j] = 1

e = floyd_warshall(csr_matrix(e))

q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    if e[s - 1][t - 1] == sys.maxsize:
        print(-1)
    else:
        print(int(e[s - 1][t - 1] - 1))
