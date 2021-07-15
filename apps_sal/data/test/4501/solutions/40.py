N,A = map(int,input().split())
ls1 = [0] + list(map(int,input().split()))

dp = [[[0 for k in range(2600)] for j in range(51) ] for i in range(51)]
for i in range(51):
    dp[i][0][0] = 1
for j in range(1,N+1):
    for k in range(1,j+1):
        for s in range(2600):
            if s < ls1[j]:
                dp[j][k][s] = dp[j-1][k][s]
            elif s >= ls1[j]:
                dp[j][k][s] = dp[j-1][k-1][s-ls1[j]] + dp[j-1][k][s]
ans = 0
for k in range(1,N+1):
    ans += dp[N][k][k*A]
print(ans)
