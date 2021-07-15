import numpy as np


def solve():
    ans = 0
    mask = 1
    for i in range(60):
        one_cnt = np.sum(A >> i & 1)
        tmp = one_cnt * (N - one_cnt)
        tmp %= MOD
        ans += tmp * mask
        ans %= MOD
        mask <<= 1
        mask %= MOD
    return ans


N, *A = list(map(int, open(0).read().split()))
A = np.array(A, dtype=np.int64)
MOD = 1_000_000_007
print((solve()))

