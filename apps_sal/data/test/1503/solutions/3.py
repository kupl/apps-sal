from sys import stdin
n,m=list(map(int,stdin.readline().strip().split()))
dp=[[-1 for i in range(n+1)] for j in range(m+1)]
for i in range(m):
    s=list(map(int,stdin.readline().strip().split()))
    for j in range(n-2,-1,-1):
        dp[i][s[j]]=s[j+1]
        
dp1=[1 for i in range(n)]
for i in range(n-2,-1,-1):
    t=True
    for j in range(m):
        if dp[j][s[i]]!=s[i+1]:
            t=False
    if t:
        dp1[i]=dp1[i]+dp1[i+1]
print(sum(dp1))
            

