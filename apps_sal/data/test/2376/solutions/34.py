from collections import *
(N, W) = map(int, input().split())
dp = defaultdict(int)
dp[0] = 0
for n in range(N):
    (w, v) = map(int, input().split())
    for (k, b) in dp.copy().items():
        if k + w <= W:
            dp[k + w] = max(dp[k + w], b + v)
print(max(dp.values()))
