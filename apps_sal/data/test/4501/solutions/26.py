def abc044_c():
    (N, A) = map(int, input().split())
    X = list(map(lambda x: int(x) - A, input().split()))
    dp = [dict() for _ in range(N + 1)]
    dp[0][0] = 1
    for (i, x) in enumerate(X):
        dp[i + 1] = dp[i].copy()
        for (val, cnt) in dp[i].items():
            dp[i + 1][val + x] = dp[i].get(val + x, 0) + cnt
    ans = dp[N][0] - 1
    print(ans)


def __starting_point():
    abc044_c()


__starting_point()
