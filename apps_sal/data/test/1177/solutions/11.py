(N, S) = list(map(int, input().split()))
A = list(map(int, input().split()))
mod = 998244353
ans = 0
dp = [0] * S
for (i, a) in enumerate(A):
    dp[0] += 1
    if a > S:
        continue
    ans = (ans + dp[S - a] * (N - i) % mod) % mod
    for (j, x) in enumerate(dp[:S - a]):
        dp[j + a] += x
print(ans)
