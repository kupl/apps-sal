n=int(input())
a=list(map(int,input().split()))
import numpy as np
dp=np.full((3,n+1),-pow(10,15))
dp[:,0]=0
dp[1,1]=a[0]
for i in range(2,n+1):
    #l,r=max(1,n//2-(n-i+1)//2),(i+1)//2+1
    l,r=max(1,i//2-1),(i+1)//2+1
    if i%3==2:
        now,pre,prepre=2,1,0
    elif i%3==0:
        now,pre,prepre=0,2,1
    elif i%3==1:
        now,pre,prepre=1,0,2
    dp[now,l:r]=np.maximum(dp[pre,l:r],dp[prepre,l-1:r-1]+a[i-1])
print(dp[now,n//2])
