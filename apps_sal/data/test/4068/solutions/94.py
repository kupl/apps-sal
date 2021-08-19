(n, m) = map(int, input().split())
A = [1] * (n + 1)
dp = [0] * (n + 1)
dp[0] = 1
for i in range(m):
    A[int(input())] = 0
if A[1]:
    dp[1] = 1
for i in range(2, n + 1):
    if A[i]:
        dp[i] = dp[i - 1] + dp[i - 2]
mod = 7 + 10 ** 9
print(dp[-1] % mod)
