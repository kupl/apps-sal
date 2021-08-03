import numpy as np

N, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB = sorted(AB)

can_add = [0] * N
for n in range(N - 1, 0, -1):
    x = can_add[n]
    y = AB[n][1]
    can_add[n - 1] = x if x > y else y

dp = np.zeros(T, np.int64)
ans = 0
for i, (a, b) in enumerate(AB):
    np.maximum(dp[a:], dp[:-a].copy() + b, out=dp[a:])
    x = dp.max() + can_add[i]
    if ans < x:
        ans = x
print(ans)
