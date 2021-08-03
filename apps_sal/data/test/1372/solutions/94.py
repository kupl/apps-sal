(h, n), *c = [[*map(int, i.split())]for i in open(0)]
dp = [0] * 20002
for i in range(h):
    dp[i] = min(dp[i - a] + b for a, b in c)
print(dp[h - 1])
