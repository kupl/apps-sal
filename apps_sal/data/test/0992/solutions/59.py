import numpy as np
import numba
from typing import List


@numba.jit
def solver(N: int, S: int, A: np.array) -> int:
    dp = np.zeros((N + 1, S + 1), dtype=np.int64)

    dp[0, 0] = 1
    MOD = 998244353
    for i in range(N):
        for j in range(S + 1):
            dp[i + 1, j] += 2 * dp[i, j]
            dp[i + 1, j] %= MOD
            if j + A[i] <= S:
                dp[i + 1, j + A[i]] += dp[i, j]
                dp[i + 1, j + A[i]] %= MOD
    return dp[N, S]


def main():
    N, S = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]

    ans = solver(N, S, np.array(A))
    print(ans)


def __starting_point():
    import sys
    sys.setrecursionlimit(10000)
    main()


__starting_point()
