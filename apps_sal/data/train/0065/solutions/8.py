from sys import stdin
t = int(stdin.readline())
for loop in range(t):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    dp = [[float('inf'), float('inf')] for i in range(n)]
    for i in range(n):
        if i == 0:
            dp[i][0] = a[0]
            continue
        elif i == 1:
            dp[i][0] = a[0] + a[1]
            dp[i][1] = dp[i - 1][0]
            continue
        dp[i][0] = min(dp[i - 2][1] + a[i - 1] + a[i], dp[i - 1][1] + a[i])
        dp[i][1] = min(dp[i - 2][0], dp[i - 1][0])
    print(min(dp[-1]))
