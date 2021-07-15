mod = 998244353
n,k = list(map(int,input().split()))
dp = [[[0,0] for i in range(2*n+1)] for j in range(n)]
dp[0][1][0] = 2
dp[0][2][1] = 2
for i in range(1,n):
	dp[i][1][0] = 2
for i in range(1,n):
	for j in range(2,k+1):
		dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j-1][0] + dp[i-1][j][1]*2) % mod
		dp[i][j][1] = (dp[i-1][j][1]+ dp[i-1][j-2][1] + dp[i-1][j-1][0]*2) % mod
# for i in dp:
# 	print (*i)
print ((sum(dp[-1][k])%mod))

# mod = 10**9+7
# n,k = map(int,input().split())
# dp = [[[0,0,0,0] for i in range(2*n+1)] for j in range(n)]
# dp[0][1][0] = 1
# dp[0][1][3] = 1
# dp[0][2][1] = 1
# dp[0][2][2] = 1
# for i in range(1,n):
# 	dp[i][1][0] = 1
# 	dp[i][1][3] = 1
# for i in range(1,n):
# 	for j in range(2,2*(i+1)+1):
# 		dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j-1][3] + dp[i-1][j][1] + dp[i-1][j][2]) % mod
# 		dp[i][j][1] = (dp[i-1][j][1] + dp[i-1][j-2][2] + dp[i-1][j-1][0] + dp[i-1][j-1][3]) % mod
# 		dp[i][j][2] = (dp[i-1][j-1][0] + dp[i-1][j-1][3] + dp[i-1][j][2] + dp[i-1][j-2][1]) % mod
# 		dp[i][j][3] = (dp[i-1][j][3] + dp[i-1][j-1][0] + dp[i-1][j][1] + dp[i-1][j][2]) % mod
# # for i in dp:
# # 	print (*i)
# print (sum(dp[-1][k])%mod)

