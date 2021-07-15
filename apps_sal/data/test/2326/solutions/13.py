n = int(input())
arr = list(map(int, input().split()))
mod = 998244353

dp = [0] * (n + 2)
C = [[0] * (n + 2) for i in range(n + 2)]

for i in range(0, n + 1):
    C[i][0] = 1
    for j in range(1, i + 1):
        C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % mod

ans = 0
dp[n] = 1
for iter in range(0, n):
    i = n - iter - 1
    if arr[i] <= 0:
        continue
    for j in range(i + arr[i] + 1, n + 1):
        dp[i] += dp[j] * C[j - i - 1][arr[i]]
        dp[i] %= mod
    ans += dp[i]

print(ans % mod)
