from collections import defaultdict
(N, MA, MB) = map(int, input().split())
ABC = [tuple(map(int, input().split())) for i in range(N)]
INF = float('inf')
dp = defaultdict(lambda: INF)
dp[0, 0] = 0
for (a, b, c) in ABC:
    dp2 = defaultdict(lambda: INF)
    for ((pa, pb), pc) in dp.items():
        dp2[pa, pb] = min(dp2[pa, pb], pc)
        dp2[pa + a, pb + b] = min(dp2[pa + a, pb + b], pc + c)
    dp = dp2
ans = INF
for i in range(1, 401):
    ans = min(ans, dp[MA * i, MB * i])
print(-1 if ans == INF else ans)
