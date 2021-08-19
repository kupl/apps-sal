(H, N) = map(int, input().split())
A_B = [list(map(int, input().split())) for _ in range(N)]
max_a = max((a for (a, b) in A_B))
max_damege = H + max_a
dp = [0] * (max_damege + 1)
for i in range(max_damege + 1):
    dp[i] = min((dp[i - a] + b for (a, b) in A_B))
print(min(dp[H - 1:]))
