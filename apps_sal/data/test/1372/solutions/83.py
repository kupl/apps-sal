h, n = map(int, input().split())

ab_input = [list(map(int, input().split())) for i in range(n)]

max_d = max(a for a, b in ab_input)

dp = [0] * (h + max_d)
for i in range(1, h + max_d):  # dp[i-a]でi-a<0のとき影響がでないようにmax_dを足す
    dp[i] = min(dp[i - a] + b for a, b in ab_input)  # モンスターの体力を i 減らすため消耗する魔力の最小値

print(dp[h])
