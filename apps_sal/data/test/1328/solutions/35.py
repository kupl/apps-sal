
import math
import sys
readline = sys.stdin.readline

N, Ma, Mb = map(int, readline().split())
INF = 10 ** 10
dp = [[INF] * (401) for i in range(401)]
dp[0][0] = 0

for _ in range(N):
    a, b, c = map(int, readline().split())
    for i in range(len(dp) - 1, -1, -1):
        for j in range(len(dp[i]) - 1, -1, -1):
            if dp[i][j] == INF:
                continue
            if dp[i + a][j + b] > dp[i][j] + c:
                dp[i + a][j + b] = dp[i][j] + c

ans = INF
for i in range(1, len(dp)):
    for j in range(1, len(dp)):
        g = math.gcd(i, j)
        if i // g == Ma and j // g == Mb:
            if ans > dp[i][j]:
                ans = dp[i][j]

if ans == INF:
    print(-1)
else:
    print(ans)
