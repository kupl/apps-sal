import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    N = input() + "0"

    dp = [[f_inf] * 2 for _ in range(len(N) + 1)]
    dp[0][0] = 0
    dp[0][1] = 1
    for i in range(1, len(N) + 1):
        n = int(N[i - 1])
        dp[i][0] = min(dp[i - 1][0] + n, dp[i - 1][1] + (10 - n))
        dp[i][1] = min(dp[i - 1][0] + n + 1, dp[i - 1][1] + (10 - n - 1))

    print((dp[-1][0]))


def __starting_point():
    resolve()

__starting_point()
