import numpy as np
H,N=list(map(int, input().split()))
A=[]
B=[]
for i in range(N):
    a,b=list(map(int, input().split()))
    A.append(a)
    B.append(b)

A=np.array(A)
B=np.array(B)
dp=np.ones((H+1+10**4))*np.inf
dp[H+1:]=0
dp[0]=0
for i in range(1,H+1):
    
    dp[i]=min(dp[i-A]+B)

print((int(dp[H])))
#print(dp)

