x=int(input())

dp=[[0 for n in range(10)] for n in range(10)]
dp1=dp.copy()

for n in range(x+1):
    v=str(n)
    p=int(v[0])
    q=int(v[-1])
    for a in range(10):
        for b in range(10):
            if a==p and b==q:
                dp[a][b]+=1

res=-1

for n in range(10):
    for k in range(10):
        res+=dp[n][k]*dp[k][n]

print(res)

