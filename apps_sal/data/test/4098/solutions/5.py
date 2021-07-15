n, k = list(map(int, input().split()))

a = list(map(int, input().split()))

a.sort()

dp = [[0 for j in range(k + 1)] for i in range(n + 1)]

l = [0 for i in range(n + 1)]

i, li = n - 1, n - 1
while i >= 0:
	while li >= 0 and a[i] - 5 <= a[li]:
		li -= 1
	l[i + 1] = li + 1
	i -= 1

dp[1][1] = 1

for i in range(2, n + 1):
	for j in range(1, k + 1):
		dp[i][j] = max(dp[i - 1][j], dp[l[i]][j - 1] + i - l[i])

print(max(dp[n][j] for j in range(1, k + 1)))

