import numpy as np

n, t = map(int, input().split())
a = []
b = []

for _ in range(n):
    a_tmp, b_tmp = map(int, input().split())
    a.append(a_tmp)
    b.append(b_tmp)

arg = np.argsort(a)
a = np.array(a)[arg]
b = np.array(b)[arg]
dp = np.zeros((n, t), dtype=np.int)

for i in range(n - 1):
    dp[i + 1, :a[i]] = dp[i, :a[i]]
    dp[i + 1, a[i]:] = np.maximum(dp[i, a[i]:], dp[i, :-a[i]] + b[i])

print(np.max(dp[:, -1] + b))
