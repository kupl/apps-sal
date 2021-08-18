
import numpy as np
N, K = list(map(int, input().split()))
KK = 2 * K
hope = np.zeros((KK, KK), dtype=np.int32)

XYC = [input().split() for _ in range(N)]

for x, y, c in XYC:
    x = int(x)
    y = int(y)
    if c == 'B':
        x -= K
    x %= KK
    y %= KK
    hope[x, y] += 1
A = np.zeros((KK + K, KK + K), dtype=np.int32)
A[:-K, :-K] = hope[:]
A[K:, :-K] += -hope[:]
A[:-K, K:] += -hope[:]
A[K:, K:] += hope[:]
A = A.cumsum(axis=0).cumsum(axis=1)

B = A[:, :KK]
B[:, :K] += A[:, KK:]
A = B[:KK, :]
A[:K, :] += B[KK:, :]
B = A[:K, :]
B[:, :K] += A[K:, K:]
B[:, K:] += A[K:, :K]

answer = B.max()
print(answer)
