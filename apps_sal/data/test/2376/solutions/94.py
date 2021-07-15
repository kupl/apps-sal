from collections import defaultdict

n, W = list(map(int, input().split()))
wv = [list(map(int, input().split())) for _ in range(n)]

dp = defaultdict(int)
dp[0] = 0

for w, v in wv:
    for k in sorted(list(dp.keys()), reverse=True):
        if k + w <= W:
            dp[k + w] = max(dp[k + w], dp[k] + v)

ans = max(dp.values())
print(ans)

