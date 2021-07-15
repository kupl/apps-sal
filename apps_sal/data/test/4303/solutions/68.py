from collections import deque
    
N,K=map(int,input().strip().split())
x=list(map(int,input().strip().split()))
inf=10**9
    
l=inf
dp=deque(x[N-K:N])
i=0
while True:
    if dp[0]>=0:
        tmp=dp[K-1]
    elif dp[K-1]<=0:
        tmp=-dp[0]
    else:
        if abs(dp[K-1])>=abs(dp[0]):
            tmp=abs(dp[0])*2+abs(dp[K-1])
        else:
            tmp=abs(dp[K-1])*2+abs(dp[0])
    l=min(l,tmp)
    i+=1
    if N-K-i<0:
        break
    else:
        dp.appendleft(x[N-K-i])
        dp.pop()
print(l)
