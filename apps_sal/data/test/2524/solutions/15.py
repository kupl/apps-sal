import numpy as np
N, *A = map(int, open(0).read().split())
A = np.array(A, dtype=np.int64)
mod = 10**9 + 7

ans = 0
for i in range(60):
    mask = 1 << i
    cnt = np.count_nonzero(A & mask)
    x = cnt * (N - cnt)
    x *= mask % mod
    ans += x
    ans %= mod

print(ans)
