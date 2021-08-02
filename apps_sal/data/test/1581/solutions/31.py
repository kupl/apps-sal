import numpy as np

n, k = list(map(int, input().split()))
mod = 10 ** 9 + 7

mx = np.sqrt(n).astype(int)

dp_u = np.ones(mx, np.int64)

N = np.full(mx, n, np.int64)
RNG = np.arange(1, mx + 2)
L = N // RNG[:-1]
R = N // RNG[1:]
R[-1] = np.maximum(R[-1], mx)
coef = L - R
dp_d = coef

for _ in range(2, k + 1):
    acc_u = np.cumsum(dp_u) % mod
    acc_d = np.cumsum(dp_d[::-1])[::-1] % mod
    dp_u = (dp_u.sum() + acc_d) % mod
    dp_d = coef * acc_u % mod

ans = (dp_u.sum() + dp_d.sum()) % mod
print(ans)
