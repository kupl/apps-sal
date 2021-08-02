def solve():
    N = input()

    INF = 10 ** 32

    dp = [[INF, INF] for i in range(len(N) + 1)]
    dp[0][0] = 0

    for i, x in enumerate(int(n) for n in N[::-1]):
        ni = i + 1
        dp[ni][0] = min(dp[i][0] + x, dp[i][1] + x)
        dp[ni][1] = min(dp[i][0] + 11 - x, dp[i][1] + 9 - x)

    ans = min(dp[-1])

    print(ans)


solve()
