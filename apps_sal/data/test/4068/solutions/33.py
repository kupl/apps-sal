(n, m) = list(map(int, input().split()))
A = []
broken = [True] * n
for i in range(m):
    a = int(input())
    A.append(a)
    broken[a] = False
dp = [0] * (n + 1)
dp[0] = 1
mod = 10 ** 9 + 7
for i in range(1, n + 1):
    if broken[i - 1]:
        dp[i] += dp[i - 1]
    if i >= 2 and broken[i - 2]:
        dp[i] += dp[i - 2]
    dp[i] %= mod
print(dp[n])
