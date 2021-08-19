from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
from array import array
from collections import deque
import sys
3


def input():
    return sys.stdin.readline().rstrip('\n')


(N, M, L) = list(map(int, input().split()))
C = [[0] * N for _ in range(N)]
for i in range(M):
    (a, b, c) = list(map(int, input().split()))
    if c > L:
        continue
    C[a - 1][b - 1] = c
Q = int(input())
ST = [None] * Q
for i in range(Q):
    (s, t) = list(map(int, input().split()))
    ST[i] = (s - 1, t - 1)
(dist_matrix, predecessors) = floyd_warshall(csgraph=C, directed=False, return_predecessors=True)
for i in range(N):
    for j in range(i + 1, N):
        if dist_matrix[i][j] <= L:
            C[i][j] = 1
(dist_matrix, predecessors) = floyd_warshall(csgraph=C, directed=False, return_predecessors=True)
for q in range(Q):
    (i, j) = ST[q]
    step = dist_matrix[i][j]
    if step > 10 ** 9:
        print(-1)
    else:
        print(int(step - 1))
