from itertools import permutations
import numpy as np
(N, C) = map(int, input().split())
D = np.ndarray((C, C), dtype=int)
c = np.ndarray((N, N), dtype=int)
for i in range(C):
    D[i] = list(map(int, input().split()))
for i in range(N):
    c[i] = list(map(int, input().split()))
c -= 1
acc = np.zeros((3, C), dtype=int)
for i in range(N):
    for j in range(N):
        acc[(i + j) % 3] += D[c[i][j]]
ans = float('inf')
for (i, j, k) in permutations(range(C), r=3):
    ans = min(ans, acc[0][i] + acc[1][j] + acc[2][k])
print(ans)
