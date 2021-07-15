h, n = map(int, input().split())
magics = [list(map(int, input().split())) for _ in range(n)]
max_damage = max(a for a, b in magics)
dp = [0] * (h + max_damage)
for i in range(1, h + max_damage):
    dp[i] = min(dp[i - a] + b for a, b in magics)
print(dp[h])
