import sys
import numba as nb
import numpy as np
input = sys.stdin.readline


@nb.njit('i8(i8,i8,i8[:,:])', cache=True)
def solve(H, N, AB):
    INF = 10 ** 18
    dp = [INF] * (H + 1)
    dp[0] = 0
    for i in range(N):
        (A, B) = AB[i]
        for d in range(H + 1):
            if d < A:
                dp[d] = min(dp[d], B)
            else:
                dp[d] = min(dp[d], dp[d - A] + B)
    ans = dp[-1]
    return ans


def main():
    (H, N) = list(map(int, input().split()))
    AB = np.zeros(shape=(N, 2), dtype=np.int64)
    for i in range(N):
        AB[i] = input().split()
    ans = solve(H, N, AB)
    print(ans)


def __starting_point():
    main()


__starting_point()
