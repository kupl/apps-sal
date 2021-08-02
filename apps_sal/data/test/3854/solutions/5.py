n, k = map(int, input().split())

dp = []
k += 1
for i in range(2):
    a = []
    for j in range(k):
        a.append([0] * k)
    dp.append(a)
dp[1][0][0] = 1

c = list(map(int, input().split()))
c = sorted(c)
for i in range(n):
    for j in range(c[i], k):
        for t in range(j + 1):
            if t >= c[i] and dp[1][j - c[i]][t - c[i]] > 0:
                dp[0][j][t] = 1
            if dp[1][j - c[i]][t] > 0:
                dp[0][j][t] = 1
    for j in range(k):
        for t in range(j + 1):
            if dp[0][j][t]:
                dp[1][j][t] = 1
    if sum(dp[1][k - 1]) == k:
        break
print(sum(dp[1][k - 1]))
for i in range(k):
    if dp[1][k - 1][i]:
        print(i)
