n = int(input())
K = input()
m = len(K)

inf = 10 ** 100

dp = [inf] * (m + 1)
dp[0] = 0

for i in range(m):
	if K[i] == '0':
		dp[i + 1] = min(dp[i + 1], dp[i] * n + int(K[i]))
	else:
		val = 0
		for j in range(i, m):
			val = val * 10 + int(K[j])
			if val >= n: break
			dp[j + 1] = min(dp[j + 1], dp[i] * n + val)

print(dp[m])


