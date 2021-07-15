import numpy as np
n,a=map(int,input().split())
x=list(map(int,input().split()))
s=sum(x)
dp=np.zeros((n,s+1),dtype=np.int64)
for i in range(n):
    for j in range(i)[::-1]:
        dp[j+1][x[i]:]+=dp[j][:-x[i]]
    dp[0][x[i]]+=1
t=0
for k in range(n):
    if (k+1)*a<=s:
        t+=dp[k][(k+1)*a]
print(t)
