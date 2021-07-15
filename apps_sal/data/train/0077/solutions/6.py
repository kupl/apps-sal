import sys
input = sys.stdin.readline
q = int(input())
for _ in range(q):
    n = int(input())
    d = [[-100, 0]] + [list(map(int, input().split())) for _ in range(n)]
    dp = [[100 for j in range(3)] for i in range(n+1)]
    dp[0] = [0, 0, 0, 0]
    for i in range(n):
        if d[i+1][0] == d[i][0]:
            dp[i+1][0] = min(dp[i][1], dp[i][2])
            dp[i+1][1] = min(dp[i][0], dp[i][2]) + d[i+1][1]
            dp[i+1][2] = min(dp[i][0], dp[i][1]) + d[i+1][1] * 2
        elif d[i+1][0] + 1 == d[i][0]:
            dp[i+1][0] = min(dp[i])
            dp[i+1][1] = min(dp[i][1], dp[i][2]) + d[i+1][1]
            dp[i+1][2] = min(dp[i][0], dp[i][1]) + d[i+1][1] * 2
        elif d[i+1][0] + 2 == d[i][0]:
            dp[i+1][0] = min(dp[i])
            dp[i+1][1] = min(dp[i]) + d[i+1][1]
            dp[i+1][2] = min(dp[i][1], dp[i][2]) + d[i+1][1] * 2
        elif d[i+1][0] - 1 == d[i][0]:
            dp[i+1][0] = min(dp[i][0], dp[i][2])
            dp[i+1][1] = min(dp[i][1], dp[i][0]) + d[i+1][1]
            dp[i+1][2] = min(dp[i]) + d[i+1][1] * 2
        elif d[i+1][0] - 2 == d[i][0]:
            dp[i+1][0] = min(dp[i][0], dp[i][1])
            dp[i+1][1] = min(dp[i]) + d[i+1][1]
            dp[i+1][2] = min(dp[i]) + d[i+1][1] * 2
        else:
            dp[i+1][0] = min(dp[i])
            dp[i+1][1] = min(dp[i]) + d[i+1][1]
            dp[i+1][2] = min(dp[i]) + d[i+1][1] * 2
    print(min(dp[n]))

