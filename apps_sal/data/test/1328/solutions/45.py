import numpy as np
(n, ma, mb) = map(int, input().split())
L = 10 * n
dp = np.zeros((L + 1, L + 1), dtype='int64')
dq = np.zeros((L + 1, L + 1), dtype='int64')
inf = 10 ** 18
dp += inf
dp[0][0] = 0
for i in range(n):
    (a, b, c) = map(int, input().split())
    dq = dp.copy()
    dq[a:, b:] = np.minimum(dq[a:, b:], dp[:-a, :-b] + c)
    dp = dq
ans = inf
for i in range(1, 401):
    if ma * i > L or mb * i > L:
        break
    ans = min(ans, dp[ma * i][mb * i])
if ans == inf:
    print(-1)
else:
    print(ans)
