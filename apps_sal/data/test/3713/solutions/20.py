n = int(input())
s = input()

dp = [1]*n

for i in range(1,n):
    if s[i]!=s[i-1]:
        dp[i] = max(dp[i], dp[i-1] + 1)
    else:
        dp[i] = dp[i-1]

print(min(n, max(dp)+2))

