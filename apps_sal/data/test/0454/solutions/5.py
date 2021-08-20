def f(n, k):
    md = 10 ** 9 + 7
    if k % 2:
        print(0)
        return
    k //= 2
    dp = [[[0] * (n + 2) for _ in range(n ** 2)] for __ in range(n + 1)]
    dp[0][0][0] = 1
    for i in range(1, n + 1):
        dpi1 = dp[i - 1]
        for j in range(i + 1):
            for s in range(j, k + 1):
                dpi1sj = dpi1[s - j]
                if j:
                    dp[i][s][j] = (dpi1sj[j] * (j * 2 + 1) + dpi1sj[j + 1] * (j + 1) ** 2 + dpi1sj[j - 1]) % md
                else:
                    dp[i][s][j] = (dpi1sj[j] * (j * 2 + 1) + dpi1sj[j + 1] * (j + 1) ** 2) % md
    print(dp[n][k][0])


(n, k) = list(map(int, input().split()))
f(n, k)
