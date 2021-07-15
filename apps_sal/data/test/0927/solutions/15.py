N,M=map(int,input().split())
A=list(map(int,input().split()))

dp=[0]*(N+1)
cost=[0,2,5,5,4,5,6,3,7,6]
for i in range(1,N+1):
    for a in A:
        if i-cost[a]>=0:
            if dp[i-cost[a]]==0 and i-cost[a]>0:
                continue
            dp[i]=max(dp[i],dp[i-cost[a]]*10+a)
print(dp[-1])
