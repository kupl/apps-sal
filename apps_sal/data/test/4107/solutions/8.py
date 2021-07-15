
n, k = list(map(int, input().split()))
mask = list(map(int, input()))

dp = [0] * (n + 2)
nxt = [1 << 31] * (n + 2)

for i in range(n, 0, -1):
    nxt[i] = i if mask[i - 1] is 1 else nxt[i + 1]

for i in range(1, n + 1):
    dp[i] = dp[i - 1] + i
    idx = nxt[max(1, i - k)]
    if idx <= i + k:
        dp[i] = min(dp[i], dp[max(0, idx - k - 1)] + idx)

print(dp[n])


