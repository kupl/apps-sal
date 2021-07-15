N=100005
lis=[0]*N
dp=[0]*N
input()
for i in map(int,input().split(' ')):
    lis[i]+=1
dp[1]=lis[1]
for i in range(2,N):
    dp[i]=max(dp[i-1],dp[i-2]+i*lis[i])
print(dp[N-1])


