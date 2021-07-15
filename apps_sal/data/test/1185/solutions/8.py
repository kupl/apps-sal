n,m,k=list(map(int, input().split()))
a=list(int(x) for x in input().split())
if m == 1:
	a.sort()
	print(sum(a[n-k:n]))
	return
s=list(sum(a[i:i+m]) for i in range(0,n-m+1))
dp=[[-1 for j in range(k+1)] for i in range(n+1)]
for i in range(n+1):
	dp[i][0]=0
for i in range(n+1):
	for j in range(1, k+1):
		dp[i][j]=dp[i-1][j]
		if i-m>=0 and dp[i-m][j-1]!=-1:
			dp[i][j]=max(dp[i][j],dp[i-m][j-1]+s[i-m])
print(dp[n][k])

