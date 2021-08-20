(n, m) = map(int, input().split())
a = set([int(input()) for i in range(m)])
dp = [0] * (10 ** 5 + 5)
dp[0] = 1
for i in range(1, n + 1):
    if i not in a:
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= 10 ** 9 + 7
print(dp[n])
