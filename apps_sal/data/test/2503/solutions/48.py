import numpy as np
import sys
(N, K) = map(int, input().split())
K2 = K * 2
Mij = [[0 for _ in range(K2 + 1)] for _ in range(K2 + 1)]


def imos(i1, j1, i2, j2):
    Mij[i1][j1] += 1
    Mij[i1][j2] -= 1
    Mij[i2][j1] -= 1
    Mij[i2][j2] += 1


for _ in range(N):
    (i, j, s) = sys.stdin.readline().split()
    i = int(i) % K2
    j = int(j) % K2
    if s == 'B':
        i = (i + K) % K2
    i1 = i % K
    j1 = j % K
    if i < K and j < K or (K <= i and K <= j):
        imos(0, 0, i1, j1)
        imos(0, j1 + K, i1, K2)
        imos(i1 + K, 0, K2, j1)
        imos(i1 + K, j1 + K, K2, K2)
        imos(i1, j1, i1 + K, j1 + K)
    else:
        imos(0, j1, i1, j1 + K)
        imos(i1 + K, j1, K2, j1 + K)
        imos(i1, 0, i1 + K, j1)
        imos(i1, j1 + K, i1 + K, K2)
Mij = np.array(Mij)
for x in range(K2):
    Mij[:, x + 1] += Mij[:, x]
for y in range(K2):
    Mij[y + 1, :] += Mij[y, :]
print(Mij.max())
