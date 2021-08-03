n = int(input())
dp = [0] + [1e9 + 7] * (n)
for i in range(1, n + 1):
    tmp = i
    while tmp:
        dp[i] = min(dp[i], dp[i - tmp % 10] + 1)
        tmp //= 10
print(int(dp[n]))
