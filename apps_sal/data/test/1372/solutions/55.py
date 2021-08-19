import numpy as np
from numba import njit, i8


@njit(i8(i8, i8, i8[:, :]), cache=True)
def solve(H, N, magics):
    dp = np.full(H + 1, 1 << 31, dtype=np.int64)
    dp[0] = 0
    for i in range(N):
        (A, B) = magics[i]
        for h in range(H):
            dp[min(h + A, H)] = min(dp[min(h + A, H)], dp[h] + B)
    return dp[-1]


(H, N, *AB) = list(map(int, open(0).read().split()))
magics = np.array([(A, B) for (A, B) in zip(*[iter(AB)] * 2)], dtype=np.int64)
print(solve(H, N, magics))
