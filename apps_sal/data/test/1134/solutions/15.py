n = int(input())
l = list(map(int,input().split()))
dp = [1 for i in range(n)]
m=0
for i in range(1,n):
    dp[i] = max(dp[i-1],l[i]+1)
for i in range(n-2,-1,-1):
    dp[i] = max(dp[i],dp[i+1]-1)
ans=0
for i in range(n):
    ans+=dp[i]-l[i]-1
print(ans)
