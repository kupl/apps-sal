n = int(input())
dp = [1]
for i in range(n):
    c = input()
    if c == 'f':
        dp.append(0)
    else:
        for j in range(1, len(dp)):
            dp[j] = (dp[j] + dp[j - 1]) % 1000000007
print(dp[-1])
