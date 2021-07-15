mod=1000000007
dp=[1]*2001
for i in range(3,2001):
	for j in range(i+3,2001):
		dp[j]=(dp[j]+dp[i])%mod
n=int(input())
if n<3:print(0)
else:print(dp[n])
