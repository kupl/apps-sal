import numpy as np
N, ma, mb = list(map(int, input().split()))
abc = tuple(list(map(int, input().split())) for _ in range(N))

inf = 10000
dp = np.full((401, 401), inf, dtype=int)
dp[0][0] = 0

for a, b, c in abc:
    for i in range(400, a - 1, -1):
        dp[i][b:] = np.minimum(dp[i][b:], dp[i - a][: - b] + c)

ans = inf
x = 1

while True:
    Ma = x * ma
    Mb = x * mb
    if Ma > 400 or Mb > 400:
        break
    ans = min(ans, dp[Ma][Mb])
    x += 1

ans = -1 if ans >= inf else ans
print(ans)

