N,A = list(map(int,input().split()))
X = list(map(int,input().split()))
dp = [[[0 for _ in range(50*(N+2))] for _ in range(N+2)] for _ in range(N+2)]

dp[0][0][0] = 1
#kまでみた
for k in range(N):
    #used個使った
    for used in range(N):
        for i in range(50*N):
            #使う時
            if dp[used][k][i] == 0: 
                continue
            dp[used+1][k+1][i+X[k]] += dp[used][k][i]
            dp[used][k+1][i] += dp[used][k][i]
ans = 0
for used in range(1,N+1):
    ans += dp[used][N][used*A]
print(ans)



