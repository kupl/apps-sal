import numpy as np
MOD = 10 ** 9 + 7
N, K = list(map(int, input().split()))
gcds = np.zeros((K + 1,), dtype=np.int64)
for n in range(K, 0, -1):
    gcds[n] = (pow(K // n, N, MOD) - gcds[np.arange(1, K // n + 1, dtype=np.int64) * n].sum()) % MOD
print((gcds @ np.arange(K + 1, dtype=np.int64) % MOD))
