def main():
    (h, w, k) = list(map(int, input().split()))
    dp = [[0] * (w + 2) for _ in range(h + 1)]
    dp[0][1] = 1
    c = [1, 1, 2, 3, 5, 8, 13, 21]
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            dp[i][j] = c[j - 1] * c[w - j] * dp[i - 1][j] + c[j - 1] * c[w - j - 1] * dp[i - 1][j + 1] + c[j - 2] * c[w - j] * dp[i - 1][j - 1]
    print(dp[h][k] % (10 ** 9 + 7))


def __starting_point():
    main()


__starting_point()
