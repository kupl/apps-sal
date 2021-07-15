import sys

import numba as nb
import numpy as np

input = sys.stdin.readline
P = 10 ** 9 + 7


@nb.njit("i8(i8[:],i8)", cache=True)
def solve(L, N):
    dp = np.zeros(shape=(N + 1, 2), dtype=np.int64)
    dp[0][0] = 1
    for i in range(N):
        n = L[i]
        for j in range(2):
            max_d = 1 if j == 1 else n
            for d in range(max_d + 1):
                next_j = int(j or d < n)
                dp[i + 1][next_j] += (d + 1) * dp[i][j]

        dp[i + 1][0] %= P
        dp[i + 1][1] %= P

    return (dp[N][0] + dp[N][1]) % P


def main():
    L = np.array(list(map(int, input().rstrip())), dtype=np.int64)

    N = len(L)
    ans = solve(L, N)

    print(ans)


def __starting_point():
    main()

__starting_point()
