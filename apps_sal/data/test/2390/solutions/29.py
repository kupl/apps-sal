n, c = list(map(int, input().split()))
x = [0]*(n+2)
v = [0]*(n+2)
for i in range(1, n+1):
    x[i], v[i] = list(map(int, input().split()))
x[n+1] = c
dp = [[0]*100100 for _ in range(2)]

ans = 0
cal = 0
for i in range(1, n+1):
    cal -= x[i] - x[i-1]
    cal += v[i]
    dp[0][i] = max(dp[0][i-1], cal)

cal = 0
for i in range(n, 0, -1):
    cal -= x[i+1] - x[i]
    cal += v[i]
    dp[1][i] = max(dp[1][i+1], cal)

ans = 0
for i in range(n+1):
    cal = dp[0][i] + dp[1][i+1] - x[i]
    ans = max(ans, cal)

    cal = dp[0][i] + dp[1][i+1] - c + x[i+1]
    ans = max(ans, cal)
print(ans)

