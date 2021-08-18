def main():
    INF = 10 ** 18
    N = int(input())
    A = list(map(int, input().split(' ')))
    K = 1 + N % 2
    dp = [[- INF for _ in range(K + 1)] for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(K + 1):
            if j < K:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
            now = dp[i][j]
            if (i + j) % 2 == 0:
                now += A[i]
            dp[i + 1][j] = max(dp[i + 1][j], now)
    print((dp[N][K]))


def __starting_point():
    main()


__starting_point()
