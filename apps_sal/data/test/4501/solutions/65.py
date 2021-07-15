import numpy as np
n,avea=tuple([int(x) for x in input().split()])
x=list([int(x) for x in input().split()])
x=np.array(x)
x=x-avea
w=max(abs(min(x)),abs(max(x)))*n
dp=np.zeros((n+1,2*w+1),dtype=int)
dp[0,w]=1
for i in range(1,n+1):
    for j in range(2*w+1):
        if 0<=j-x[i-1]<=2*w:
            dp[i,j]=dp[i-1,j]+dp[i-1,j-x[i-1]]
        else:
            dp[i,j]=dp[i-1,j]
print((dp[n,w]-1))

