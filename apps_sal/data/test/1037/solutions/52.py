import numpy as np
from collections import defaultdict
n = int(input())
a_ = list(map(int, input().split()))
a = []
for i, ai in enumerate(a_):
    a.append([1 + i, ai])
a.sort(key=lambda x: x[1], reverse=True)
dp = np.zeros((n + 1, n + 1), np.int64)
dp[1, 1] = a[0][1] * (n - a[0][0])
dp[1, 0] = a[0][1] * (a[0][0] - 1)
for i in range(2, n + 1):
    dp[i, 0] = dp[i - 1, 0] + a[i - 1][1] * abs((a[i - 1][0] - 1 - (i - 1)))
    dp[i, i] = dp[i - 1, i - 1] + a[i - 1][1] * abs((n - a[i - 1][0] - (i - 1)))
    l = dp[i - 1, 1:i] + [a[i - 1][1] * abs((a[i - 1][0] - 1 - j))for j in range(i - 2, -1, -1)]
    r = dp[i - 1, :i - 1] + [a[i - 1][1] * abs((n - a[i - 1][0] - j)) for j in range(i - 1)]
    dp[i, 1:i] = np.maximum(l, r)
print((max(dp[n])))
