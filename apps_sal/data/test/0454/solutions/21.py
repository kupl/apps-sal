def f(n, k):
    md = 10 ** 9 + 7
    if k % 2:
        print((0))
        return
    k //= 2
    dp = [[[0] * (n ** 2) for _ in range(n + 2)] for __ in range(n + 1)]
    dp[0][0][0] = 1
    for i in range(1, n + 1):
        dpi1 = dp[i - 1]
        for j in range(i + 1):
            for s in range(j, k + 1):
                tmp = dpi1[j][s - j] * j * 2 + dpi1[j][s - j] + dpi1[j + 1][s - j] * (j + 1) ** 2
                if j:
                    tmp += dp[i - 1][j - 1][s - j]
                dp[i][j][s] = tmp % md
    print((dp[n][0][k]))


n, k = list(map(int, input().split()))
f(n, k)
