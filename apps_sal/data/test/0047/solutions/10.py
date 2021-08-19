def main():
    (n, x) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    dp = [[0, 0, 0] for _ in range(n)]
    dp[0][0] = max(0, a[0])
    dp[0][1] = max(0, x * a[0])
    answer = max(dp[0])
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0] + a[i], a[i])
        dp[i][1] = max(dp[i - 1][1] + x * a[i], x * a[i], dp[i - 1][0] + x * a[i])
        dp[i][2] = max(dp[i - 1][2] + a[i], dp[i - 1][1] + a[i])
        answer = max(answer, *dp[i])
    print(answer)


def __starting_point():
    main()


__starting_point()
