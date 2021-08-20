from itertools import *
from numpy import *
from scipy.sparse.csgraph import *
(N, X, Y) = map(int, input().split())
A = (N - 1) * [0]
G = zeros((N, N))
G[X - 1][Y - 1] = 1
G[Y - 1][X - 1] = 1
for n in range(N - 1):
    G[n][n + 1] = 1
    G[n + 1][n] = 1
S = shortest_path(G)
for (i, j) in combinations(range(N), 2):
    A[int(S[i][j]) - 1] += 1
print(*A, sep='\n')
