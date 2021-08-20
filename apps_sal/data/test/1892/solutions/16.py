n = int(input())
dp = [1]
for IND in range(n):
    c = input()
    if c == 'f':
        dp.insert(0, 0)
    else:
        for i in range(len(dp) - 2, -1, -1):
            dp[i] = (dp[i] + dp[i + 1]) % 1000000007
print(dp[0])
