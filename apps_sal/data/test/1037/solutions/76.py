import heapq
import time
st = time.time()
n = int(input())
a = list(map(int, input().split()))
hq = []
for i, ai in enumerate(a):
    heapq.heappush(hq, (-ai, i))
dp = [[0 for i in range(j + 1)] for j in range(n + 1)]
dp[0][0] = 0
ai, hi = heapq.heappop(hq)
dp[1][0] = -ai * (n - 1 - hi)
dp[1][1] = -ai * hi
for i in range(2, n + 1):
    ai, hi = heapq.heappop(hq)
    dp[i][0] = dp[i - 1][0] - ai * abs(n - i - hi)
    dp[i][i] = dp[i - 1][i - 1] - ai * abs(hi - i + 1)
    for j in range(1, i):
        dp[i][j] = max(dp[i - 1][j - 1] - ai * abs(hi - j + 1), dp[i - 1][j] - ai * abs(n - i + j - hi))

print((max(dp[n])))
