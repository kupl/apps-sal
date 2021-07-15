for _ in range(int(input())):
	s = input()
	N = len(s)
	dp = [0] * (N + 1)
	for i in range(2, N):
		if s[i - 4 : i + 1] == 'twone':
			dp[i - 2] = dp[i - 3]
			dp[i + 1] = dp[i]
		elif s[i - 2 : i + 1] == 'one':
			dp[i] = dp[i - 1] + 1
			dp[i + 1] = dp[i]
		elif s[i - 2 : i + 1] == 'two':
			dp[i] = dp[i - 1] + 1
			dp[i + 1] = dp[i]
		else:
			dp[i + 1] = dp[i]
	i = N
	res = list()
	print(dp[N])
	while dp[i] != 0:
		if dp[i - 1] != dp[i]:
			res.append(i)
		i -= 1
	print(*res)

