
H, N = map(int, input().split())
ab_list = [list(map(int, input().split())) for _ in range(N)]

max_a = max(a for a, b in ab_list)
W = H + 1 + max_a
dp = [0] * W

for i in range(W):
    dp[i] = min(dp[i - a] + b for a, b in ab_list)

print(min(dp[H - 1:]))
