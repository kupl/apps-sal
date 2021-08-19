import numpy as np
(N, K) = map(int, input().split())
MOD = 10 ** 9 + 7
M = int(N ** 0.5)
upper_cnt = np.zeros(M + 1, dtype=np.int64)
a = np.arange(M + 1, dtype=np.int64)
upper_cnt[1:] = N // a[1:] - np.maximum(M, N // (a[1:] + 1))
lower = np.zeros(M + 1, dtype=np.int64)
upper = np.zeros(M + 1, dtype=np.int64)
lower[1] = 1
for k in range(1, K + 1):
    prev_lower = lower
    prev_upper = upper
    cum_lower = prev_lower.cumsum() % MOD
    cum_upper = prev_upper.cumsum() % MOD
    lower = np.zeros(M + 1, dtype=np.int64)
    lower += cum_lower[-1] + cum_upper[-1]
    lower[1:] -= cum_upper[:-1]
    lower[0] = 0
    upper = cum_lower * upper_cnt
    lower %= MOD
    upper %= MOD
answer = (lower.sum() + upper.sum()) % MOD
print(answer)
