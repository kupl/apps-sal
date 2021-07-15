
N, Ma, Mb = list(map(int,input().split()))
rate = Ma / Mb
a = [0] * N
b = [0] * N
c = [0] * N
MA = 0
MB = 0
MC = 0
for i in range(N):
    a[i], b[i], c[i] = list(map(int, input().split()))
    MA += a[i]
    MB += b[i]
    MC += c[i]
    
dp = [[[MC for i in range(MB+1)] for j in range(MA+1)] for k in range(N+1)]
dp[0][0][0] = 0

for it_N in range(N):
    for it_MA in range(MA+1):
        for it_MB in range(MB+1):
            if it_MA >= a[it_N] and it_MB >= b[it_N]:
                if dp[it_N][it_MA-a[it_N]][it_MB-b[it_N]] != MC:
                    dp[it_N+1][it_MA][it_MB] = min(dp[it_N][it_MA-a[it_N]][it_MB-b[it_N]] + c[it_N], dp[it_N][it_MA][it_MB])
                else:
                    dp[it_N+1][it_MA][it_MB]=dp[it_N][it_MA][it_MB]
            else:
                dp[it_N+1][it_MA][it_MB]=dp[it_N][it_MA][it_MB]

ans = -1
for a in range(1, MA+1):
    for b in range(1, MB+1):
        if a/b == rate and dp[N][a][b] != MC:
            if ans == -1:
                ans = dp[N][a][b]
            else:
                ans = min(dp[N][a][b], ans)
print(ans)

