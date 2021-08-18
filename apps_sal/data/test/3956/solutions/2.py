import sys


def mul(c, m, dp):
    for i in range(m, c - 1, -1):
        dp[i] += dp[i - c]
        dp[i] %= MOD


def mul2(c, m, dp):
    for i in range(m, c - 1, -1):
        dp[i] -= dp[i - c]
        dp[i] %= MOD


def div(c, m, dp):
    for i in range(m - c + 1):
        dp[i + c] += dp[i]
        dp[i + c] %= MOD


readline = sys.stdin.readline
read = sys.stdin.read

MOD = 998244353
k, n = map(int, readline().split())

ans = [0] * (2 * k + 1)
dp = [1] + [0] * n
for _ in range(k - 1):
    div(1, n, dp)
ans[2] = (dp[n - 1] + dp[n])
for i in range(3, k + 2):
    if i % 2:
        mul(1, n, dp)
        ans[i] = dp[n]
    else:
        mul2(1, n, dp)
        ans[i] = dp[n - 1] + dp[n]

for i in range(k + 2, 2 * k + 1):
    ans[i] = ans[2 + 2 * k - i]

for i in ans[2:]:
    print(i % MOD)
