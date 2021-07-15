n, m = list(map(int,input().split(' ')))
l = []
for i in range(n):
    x, y = list(map(int,input().split(' ')))
    l.append([x-y,x+y])

dp = [m for i in range(m+1)]
dp[0] = 0
for i in range(1,m+1):
    dp[i] = min(dp[i-1] + 1,dp[i])
    for j in l:
        x = max(0,j[0] - i)
        y = min(m,j[1] + x)
        dp[y] = min(dp[y],dp[i - 1] + x)

print(dp[-1])
