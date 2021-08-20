def main():
    N = int(input())
    INF = float('inf')
    dp = [INF] * (N + 1)
    dp[0] = 0
    for n in range(1, N + 1):
        dp[n] = 1 + dp[n - 1]
        for k in range(1, 8):
            p = 6 ** k
            if n - p >= 0:
                dp[n] = min(dp[n], dp[n - p] + 1)
            p = 9 ** k
            if n - p >= 0:
                dp[n] = min(dp[n], dp[n - p] + 1)
    ans = dp[N]
    print(ans)


def __starting_point():
    main()


__starting_point()
