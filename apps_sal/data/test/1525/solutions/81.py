h,w,K=map(int,input().split())
mod=10**9+7
dp=[[0 for i in range(w)] for j in range(h+1)]
for i in range(2**(w-1)):dp[0][0]=1
for i in range(1,h+1):
    for j in range(2**(w-1)):
        s=format(j,"b").zfill(w-1)
        if "11" in s:continue
        exchanged=[False]*w
        for k in range(w-1):
            if s[k]=="1":
                dp[i][k]+=dp[i-1][k+1]
                dp[i][k+1]+=dp[i-1][k]
                dp[i][k]%=mod
                dp[i][k+1]%=mod
                exchanged[k]=True
                exchanged[k+1]=True
        for k in range(w):
            if exchanged[k]:continue
            dp[i][k]+=dp[i-1][k]
            dp[i][k]%=mod

print(dp[-1][K-1])
