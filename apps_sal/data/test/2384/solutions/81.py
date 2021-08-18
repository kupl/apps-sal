def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [[[-float("inf")] * 2 for j in range(3)] for i in range(n + 1)]
    dp[0][0][0] = 0
    for i in range(n):
        x = a[i]
        if i % 2 == 0:
            for j in range(-1, 2):
                dp[i + 1][j][0] = max(dp[i][j][0], dp[i][j][1])
            for j in range(-1, 1):
                dp[i + 1][j + 1][1] = dp[i][j][0] + x
        else:
            for j in range(-1, 1):
                dp[i + 1][j][0] = max(dp[i][j + 1][0], dp[i][j + 1][1])
            for j in range(-1, 2):
                dp[i + 1][j][1] = dp[i][j][0] + x
    print(max(dp[n][0][0], dp[n][0][1]))


def __starting_point():
    main()


__starting_point()
