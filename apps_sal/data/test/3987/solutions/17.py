t = 1
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    dp = [[0 for j in range(4)] for i in range(n)]
    p1 = [0] * (n + 1)
    p2 = [0] * (n + 1)
    for i in range(n):
        p1[i + 1] += p1[i]
        p2[i + 1] += p2[i]
        if l[i] == 1:
            p1[i + 1] += 1
        else:
            p2[i + 1] += 1
    if l[0] == 1:
        dp[0][0] = 1
    else:
        dp[0][1] = 1
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if l[i] == 1:
                dp[i][0] = p1[i + 1]
                dp[i][1] = max(dp[j][1], dp[i][1])
                if dp[j][1] != 0:
                    dp[i][2] = max(dp[j][1] + 1, dp[j][2] + 1, dp[i][2])
                else:
                    dp[i][2] = max(dp[j][2] + 1, dp[i][2])
                dp[i][3] = max(dp[j][2], dp[i][3])
            else:
                dp[i][0] = max(dp[j][0], dp[i][0])
                if dp[j][0] != 0:
                    dp[i][1] = max(dp[j][1] + 1, dp[j][0] + 1, dp[i][1])
                else:
                    dp[i][1] = max(dp[j][1] + 1, dp[i][1])
                dp[i][2] = dp[j][2]
                if dp[j][2] != 0:
                    dp[i][3] = max(dp[j][3] + 1, dp[j][2] + 1, dp[i][3])
                else:
                    dp[i][3] = max(dp[j][3] + 1, dp[i][3])
    maxi = 0
    for i in range(n):
        for j in range(4):
            maxi = max(maxi, dp[i][j])
    print(maxi)
