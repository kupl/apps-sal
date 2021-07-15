n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
dp = [0]*n
start = a[0]
k,i = 0,0
while i<n:
	if a[i]-start>5:
		dp[k] = i-k
		k += 1
		start = a[k]
	else:
		i+=1
dp[k] = n-k
for i in range(k+1,n):
	dp[i] = dp[i-1]-1
# print (dp)
if dp[0]==n:
	print (n)
	return

dp2=[[0 for i in range(m+1)] for j in range(n+1)]
for i in range(n-1,-1,-1):
	for j in range(1,m+1):
		dp2[i][j] = max(dp2[i+1][j], dp2[i+1][j-1]+1, dp2[dp[i]+i][j-1]+(dp[i]))
# print (dp2)
print (dp2[0][m])
