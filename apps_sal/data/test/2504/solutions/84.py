from scipy.sparse import csgraph
from scipy.sparse import csr_matrix
(n, m, l) = list(map(int, input().split()))
d = [[10 ** 12 for i in range(n + 1)] for i in range(n + 1)]
for i in range(m):
    (x, y, z) = list(map(int, input().split()))
    d[x][y] = z
    d[y][x] = z
for i in range(n + 1):
    d[i][i] = 0
q = int(input())
que = []
for _ in range(q):
    (s, t) = list(map(int, input().split()))
    que.append((s, t))
csr = csr_matrix(d)
K = csgraph.shortest_path(csr, method='FW', directed=True)
e = [[10 ** 12 for i in range(n + 1)] for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if K[i][j] <= l:
            e[i][j] = 1
for i in range(n + 1):
    e[i][i] = 0
A = csr_matrix(e)
ANS = csgraph.shortest_path(A, method='FW', directed=True)
for some in que:
    (s, t) = (some[0], some[1])
    if int(ANS[s][t]) < 10 ** 12:
        print(int(ANS[s][t]) - 1)
    else:
        print(-1)
