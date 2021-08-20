MOD = 10 ** 9 + 7
MAX_N = 2 * 10 ** 5 + 5
dp = [[0] * 3 for i in range(MAX_N)]


def main():
    (n, l, r) = list(map(int, input().split()))
    k0 = r // 3 - (l - 1) // 3
    k1 = r // 3 + (r % 3 >= 1) - ((l - 1) // 3 + ((l - 1) % 3 >= 1))
    k2 = r // 3 + (r % 3 >= 2) - ((l - 1) // 3 + ((l - 1) % 3 >= 2))
    (dp[0][0], dp[0][1], dp[0][2]) = (k0, k1, k2)
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] * k0 + dp[i - 1][1] * k2 + dp[i - 1][2] * k1
        dp[i][1] = dp[i - 1][0] * k1 + dp[i - 1][1] * k0 + dp[i - 1][2] * k2
        dp[i][2] = dp[i - 1][0] * k2 + dp[i - 1][1] * k1 + dp[i - 1][2] * k0
        for j in range(3):
            dp[i][j] %= MOD
    print(dp[n - 1][0])


def __starting_point():
    main()


__starting_point()
