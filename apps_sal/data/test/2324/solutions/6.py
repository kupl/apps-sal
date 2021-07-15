s = input()

dp = [[0]*5005 for _ in range(5005)]
n = len(s)
ans = [0 for _ in range(5005)]

for length in range(1,n+1):
	for l in range(n-length+1):
		r = l+length
		if(length == 1):
			dp[l][r] = 1
			continue
		elif(length == 2):
			dp[l][r] = 2 if(s[l] == s[r-1]) else 0
			continue
		if(s[l] != s[r-1] or dp[l+1][r-1] == 0):
			continue
		dp[l][r] = 1
		m = (l+r) // 2
		if(length&1):
			if(dp[l][m] and dp[m+1][r]):
				dp[l][r] = dp[l][m]+1
		else:
			if(dp[l][m] and dp[m][r]):
				dp[l][r] = dp[l][m]+1

for length in range(1,n+1):
	for l in range(n-length+1):
		ans[dp[l][l+length]] += 1

for i in range(n-1,0,-1):
	ans[i] += ans[i+1]

for i in range(1,n+1):
	print(ans[i],end=' ')

print()

