s = input()
frommap = []
for d in range(10):
    frommap.append([0] * 13)
    for m in range(13):
        m2 = (m * 10 + d) % 13
        frommap[d][m2] = m
dp = [1] + [0] * 12
for c in s:
    if c == '?':
        dp = [sum((dp[f] for f in fromlist)) % 1000000007 for fromlist in zip(*frommap)]
    else:
        dp = [dp[f] for f in frommap[int(c)]]
print(dp[5])
