def main():
    n = int(input())
    tmp = list(map(int, input().split()))
    a = [[v, i] for (i, v) in enumerate(tmp)]
    a.sort(reverse=True)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        (v, idx) = a[i]
        for j in range(i + 1):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + v * abs(idx - j))
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + v * abs(idx - (n - 1 - i + j)))
    print(max(dp[n]))


def __starting_point():
    main()


__starting_point()
