n = int(input())
s = input()
dp = [0 for i in range(n + 1)]
for i in range(n):
    if s[i - dp[i]:i + 1] in s[:i - dp[i]]:
        dp[i + 1] = dp[i] + 1
    else:
        dp[i + 1] = dp[i]
print(dp[n])
