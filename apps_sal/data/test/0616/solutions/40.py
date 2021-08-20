(n, m) = map(int, input().split())
keys = []
for i in range(m):
    (a, b) = map(int, input().split())
    s = 0
    for c in map(int, input().split()):
        c -= 1
        s |= 1 << c
    keys.append((s, a))
INF = 1001001001
dp = [INF] * (1 << n)
dp[0] = 0
for s in range(1 << n):
    for (k, v) in keys:
        t = s | k
        cost = dp[s] + v
        dp[t] = min(dp[t], cost)
ans = dp[-1]
if ans == INF:
    ans = -1
print(ans)
