N = int(input())
mod = 10 ** 9 + 7
dp = [N] * (N + 1)
dp[N - 1] = N
dp[N - 2] = N * N
c = N * (N + 1) + N - 1
const = (N - 1) ** 2
for i in range(N - 3, -1, -1):
    ans = c - dp[i + 2] + const
    dp[i] = ans
    c = (c + ans - 1) % mod
print(dp[0] % mod)
