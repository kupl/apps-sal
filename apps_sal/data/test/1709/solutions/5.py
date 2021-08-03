MAX = 10**18 + 5
n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
cost = [list(map(int, input().split())) for _ in range(n)]
min1 = [[MAX] * (k + 1) for _ in range(n)]
min2 = [[MAX] * (k + 1) for _ in range(n)]
idx = [[-1] * (k + 1) for _ in range(n)]
for i in cost:
    i.insert(0, 0)
dp = [[[MAX] * (m + 1) for _ in range(k + 1)] for _ in range(n)]

if a[0] == 0:
    for i in range(1, m + 1):
        if min1[0][1] >= cost[0][i]:
            if min1[0][1] == cost[0][i]:
                idx[0][1] = -1

            else:
                idx[0][1] = i
            min2[0][1] = min1[0][1]
            min1[0][1] = cost[0][i]

        elif min2[0][1] >= cost[0][i]:
            min2[0][1] = cost[0][i]

        dp[0][1][i] = cost[0][i]
else:
    dp[0][1][a[0]] = 0
    min1[0][1] = 0
    idx[0][1] = a[0]

# print(min1)
# print(min2)
for i in range(1, n):
    for j in range(1, k + 1):
        if a[i] == 0:
            for l in range(1, m + 1):
                dp[i][j][l] = min(dp[i][j][l], dp[i - 1][j][l] + cost[i][l])
                if l == idx[i - 1][j - 1]:
                    dp[i][j][l] = min(min2[i - 1][j - 1] + cost[i][l], dp[i][j][l])
                else:
                    dp[i][j][l] = min(min1[i - 1][j - 1] + cost[i][l], dp[i][j][l])

        else:
            for l in range(1, m + 1):
                dp[i][j][a[i]] = min(dp[i][j][a[i]], dp[i - 1][j][a[i]])
                if l != a[i]:
                    dp[i][j][a[i]] = min(dp[i - 1][j - 1][l], dp[i][j][a[i]])

        for l in range(1, m + 1):
            if min1[i][j] >= dp[i][j][l]:
                if min1[i][j] == dp[i][j][l]:
                    idx[i][j] = -1

                else:
                    idx[i][j] = l
                min2[i][j] = min1[i][j]
                min1[i][j] = dp[i][j][l]

            elif min2[i][j] >= dp[i][j][l]:
                min2[i][j] = dp[i][j][l]
ans = MAX
for i in dp[-1][-1]:
    ans = min(ans, i)
print(ans if ans < MAX else -1)
