(h, n) = map(int, input().split())
magics = [tuple(map(int, input().split())) for _ in range(n)]
max_a = sorted(magics, key=lambda x: x[0], reverse=True)[0][0]
dp = [0] * (h + max_a)
for i in range(1, h + max_a):
    dp[i] = min((dp[i - a] + b for (a, b) in magics))
print(min(dp[h:]))
