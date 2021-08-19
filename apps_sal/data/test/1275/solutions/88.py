import numpy as np
(N, K) = map(int, input().split())
K = abs(K)
C = np.array([*range(-1, N), *range(N, 0, -1)], dtype=np.int64)
C[0] = 0
print(C[:-K] @ C[K:] if K else C @ C)
