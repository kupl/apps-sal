H, N = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]
max_a = max(a for a, b in ab)
dp = [0]*(H+max_a)
for i in range(1, H+max_a):
    dp[i] = min(dp[i-a]+b for a, b in ab)
print(dp[H])
