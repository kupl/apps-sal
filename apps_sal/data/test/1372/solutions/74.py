(h, n), *m = [[*list(map(int, i.split()))] for i in open(0)]
dp = [0] * 20001
for i in range(1, h + 1):
    dp[i] = min(dp[i-a]+b for a, b in m)
print((dp[h]))

