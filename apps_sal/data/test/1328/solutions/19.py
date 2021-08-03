import numpy as np

n, ma, mb = map(int, input().split())
U = 400
dp = np.full((U + 1, U + 1), float("inf"))
dp[0, 0] = 0
for i in range(n):
    a, b, c = map(int, input().split())
    np.minimum(dp[a:, b:], dp[:-a, :-b] + c, out=dp[a:, b:])
ans = float("inf")
for i in range(1, 1 + U // max(ma, mb)):
    na, nb = i * ma, i * mb
    ans = min(ans, dp[na, nb])
if ans == float("inf"):
    print(-1)
else:
    print(int(ans))
