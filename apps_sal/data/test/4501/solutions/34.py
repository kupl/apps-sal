import sys
readline = sys.stdin.readline


def main():
    N, A = map(int, readline().rstrip().split())
    X = list(map(int, readline().rstrip().split()))
    lim = max(X) * N
    X = [x - A for x in X]
    dp = [[0] * (2 * lim) for _ in range(N + 1)]
    dp[0][lim] = 1
    for i in range(1, N + 1):
        x = X[i - 1]
        for j in range(2 * lim):
            if 0 <= j - x < 2 * lim:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - x]
            else:
                dp[i][j] = dp[i - 1][j]

    print(dp[N][lim] - 1)


def __starting_point():
    main()


__starting_point()
