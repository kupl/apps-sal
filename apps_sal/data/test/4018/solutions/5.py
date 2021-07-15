n, tt = list(map(int, input().split()))
s = input()

dp = [[0]*(n + 1) for i in range(n+1)]

for c in range(n+1):
	dp[0][c] = 1

last = [-1]*26

for c in range(1, n + 1):
	k = ord(s[c-1]) - ord('a')
	for r in range(1, n+1):
		dp[r][c] = dp[r][c-1] + dp[r-1][c-1]
	if last[k] == -1:
		last[k] = c - 1
		continue
	else:
		p = last[k]
		for r in range(1, n+1):
			dp[r][c] = dp[r][c] - dp[r-1][p]
		last[k] = c-1

su, ans, t = 0, 0, 0
for r in range(n+1):
	su = su + dp[r][n]
if su < tt:
	ans = -1
else:
	for i in range(n, -1, -1):
		r = min(tt, dp[i][n])
		ans += t*r
		tt -= r
		t += 1

print(ans) 

