for haaghfj in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [[100000000000000] * 2 for i in range(n + 2)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        dp[i][0] = min(dp[i - 1][1], dp[i - 2][1])
        dp[i][1] = min(dp[i - 1][0] + a[i - 1], dp[i - 2][0] + a[i - 1] + a[i - 2])
    print(min(dp[n]))
