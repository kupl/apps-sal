N,M=map(int, input().split())
S=input()
now=S[N-1]
dp=[float("INF")]*(N+1)
dp[N]=0
nowmin=0
right=N
for left in range(N-1,-1,-1):
    while right-left>M or S[right]=="1":
        right-=1
        nowmin=dp[right]
    if right<=left:
        print(-1)
        return
    if S[left]=="1":
        continue
    else:
        dp[left]=1+nowmin
#print(dp)
#print(dp[0])
now=dp[0]
nowi=0
"""
if now==float("INF"):
    print(-1)
    return
"""
for i in range(1,N+1):
    if now>dp[i]:
        print(i-nowi, end=" ")
        now=dp[i]
        nowi=i

