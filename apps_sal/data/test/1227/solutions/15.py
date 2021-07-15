s=input()
n=len(s)

K=int(input())

dp=[[[0] * 5 for _ in range(2)] for _ in range(n+1)]
dp[0][0][0]=1

for i in range(n):
    ni= int(s[i])

    for k in range(4):
            # smaller 1 -> 全部OK
            dp[i + 1][1][k + 1] += dp[i][1][k] * 9;  
            dp[i + 1][1][k] += dp[i][1][k];  

            # smaller 0,next smaller 1 -> nowより小さいのを全部
            # 次の桁からsmallerであるためにはN＜ni であることが必要で
            # Nは0より大きい必要がある。（0より小さいものがない＝確定しない
            if (ni > 0):
                dp[i + 1][1][k + 1] += dp[i][0][k] * (ni - 1)
                dp[i + 1][1][k] += dp[i][0][k]
                
            # smaller 0,next smaller 0 -> nowだけ
            if (ni > 0) :
                dp[i + 1][0][k + 1] = dp[i][0][k]
            else:
                dp[i + 1][0][k] = dp[i][0][k]

ans=dp[n][0][K] + dp[n][1][K]
print(ans)
