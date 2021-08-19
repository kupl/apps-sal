def f(n, m):
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    dp = [[1] * (m + 1) for _ in range(n + 1)]
    for (i, sk) in enumerate(s):
        dpi1 = dp[i + 1] = dp[i][:]
        cs = 0
        for (j, tk) in enumerate(t):
            if sk == tk:
                cs = (cs + dp[i][j]) % md
            dpi1[j + 1] = (dpi1[j + 1] + cs) % md
    print(dp[-1][-1])


md = 10 ** 9 + 7
(n, m) = list(map(int, input().split()))
f(n, m)
