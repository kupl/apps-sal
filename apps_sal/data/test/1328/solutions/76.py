N,Ma,Mb = list(map(int,input().split()))

INF = float('inf')

dp = [[INF for b in range(401)] for a in range(401)]

dp[0][0] = 0

sa = 0
sb = 0

for i in range(1,N+1):
    ai,bi,ci = list(map(int,input().split()))
    sa += ai
    sb += bi
    for a in range(sa+1,-1,-1):
        for b in range(sb+1,-1,-1):
            if a-ai >= 0 and b-bi >= 0:
                dp[a][b] = min(dp[a][b],dp[a-ai][b-bi]+ci)


ans = INF
for j in range(1,401):
    if Ma*j > 400 or Mb*j > 400:
        break
    ans = min(ans,dp[Ma*j][Mb*j])
print((ans if ans != INF else -1))


