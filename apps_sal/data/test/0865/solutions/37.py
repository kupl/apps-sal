import numpy as np
(N, T) = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(N)]


def knapsack(ab):
    dp = np.zeros(T, dtype=np.int64)
    res = [dp]
    for (a, b) in ab:
        newDP = res[-1].copy()
        newDP[a:] = np.maximum(newDP[a:], newDP[:-a] + b)
        res.append(newDP)
    return res


dp1 = knapsack(AB)
dp2 = knapsack(AB[::-1])
dp2 = dp2[::-1]
ans = 0
for i in range(N):
    (_, b) = AB[i]
    l = dp1[i]
    r = dp2[i + 1][::-1]
    tmp = (l + r).max() + b
    ans = max(ans, tmp)
print(ans)
