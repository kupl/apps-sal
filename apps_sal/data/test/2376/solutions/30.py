n,W = map(int,input().split())

dp = [[[0]*(3*n+1) for _ in range(n)] for _ in range(n)]

w1,v1 = map(int,input().split())
for i in range(3*n+1):
    dp[0][0][i] = v1

for i in range(1,n):
    w,v = map(int,input().split())
    w -= w1
    for j in range(min(i+1,n)):
        for k in range(3*n+1):
            if j>0 and k>=w:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-1][k-w] + v)
            elif k>=w:
                dp[i][0][k] = max(dp[i-1][0][k], v)
            else:
                dp[i][j][k] = dp[i-1][j][k]

ans = 0
for i in range(n):
    for j in range(3*n+1):
        if w1*(i+1) + j>W: continue
        ans = max(ans,dp[-1][i][j])

print(ans)
