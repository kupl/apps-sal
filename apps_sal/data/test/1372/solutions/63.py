
h, n = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * 20001

for i in range(h):
    dp[i] = min(dp[i - a] + b for a, b in ab)
print((dp[h - 1]))
