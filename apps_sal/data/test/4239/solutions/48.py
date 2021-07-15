import math
N=int(input())
dp=[math.inf for _ in range(N+1)]
dp[0]=0
for i in range(1,N+1):
	p=1
	q=1
	while p<=i:
		dp[i]=min(dp[i],dp[i-p]+1)
		p*=6
	while q<=i:
		dp[i]=min(dp[i],dp[i-q]+1)
		q*=9
print(dp[N])
