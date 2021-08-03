from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
import numpy as np
import sys
def input(): return sys.stdin.readline().rstrip()
def inpl(): return list(map(int, input().split()))


N, M, L = inpl()
graph = [[0] * N for _ in range(N)]
for i in range(M):
    A, B, C = inpl()
    if C <= L:
        graph[A - 1][B - 1] = C

Q = int(input())
ST = []
for _ in range(Q):
    s, t = inpl()
    s -= 1
    t -= 1
    ST.append((s, t))

distance = floyd_warshall(csr_matrix(graph), directed=False)
path = [[0] * N for _ in range(N)]
for i in range(N - 1):
    for j in range(i + 1, N):
        d = distance[i][j]
        if d <= L:
            path[i][j] = 1
ans = floyd_warshall(csr_matrix(path), directed=False)
for s, t in ST:
    if ans[s][t] == np.float('inf'):
        print((-1))
    else:
        print((int(ans[s][t] - 1)))
