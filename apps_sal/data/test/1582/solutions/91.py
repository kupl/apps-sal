def main():
    n = int(input())
    dp = [[0 for i in range(10)] for i in range(10)]
    for i in range(1, n + 1):
        h, t = int(str(i)[0]), int(str(i)[-1])
        dp[h][t] += 1
    ans = 0
    for i in range(10):
        for j in range(10):
            ans += dp[i][j] * dp[j][i]
    print(ans)


def __starting_point():
    main()


__starting_point()
