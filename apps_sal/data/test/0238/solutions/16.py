#Bhargey Mehta (Junior)
#DA-IICT, Gandhinagar
import sys, math, queue
#sys.stdin = open('input.txt', 'r')
MOD = 998244353
sys.setrecursionlimit(1000000)

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [[-10**20 for i in range(m)] for i in range(n)]
dp[0][0] = a[0]-k

for i in range(1, n):
	for j in range(m):
		if j == 0:
			dp[i][j] = max(dp[i-1][m-1]+a[i], a[i])-k
		else:
			dp[i][j] = dp[i-1][j-1]+a[i]

ans = 0
for i in range(n):
	ans = max(ans, max(dp[i]))
print(ans)
