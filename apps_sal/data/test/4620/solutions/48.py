n = int(input())
cost = [0]*n
start = [0]*n
freaq = [0]*n
dp = [[0]*n for _ in range(n)]

for i in range(n-1):
    cost[i],start[i],freaq[i] = map(int,input().split())
    dp[i][i] = start[i]

freaq[n-1] = 1

t = 0

for i in range(n-1):
    for j in range(i+1):
        t = dp[j][i]
        t += cost[i]
        if t%freaq[i+1] != 0:
            t += freaq[i+1] - t%freaq[i+1]
        t = max(t,start[i+1])
        dp[j][i+1] = t

for i in range(n):
    print(dp[i][n-1])
