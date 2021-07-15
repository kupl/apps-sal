import numpy as np
def solve(n, t, a, b):
    dp = np.zeros(t, dtype=int)
    candidates = []
    for w, v in sorted(zip(a, b)):
        candidates.append(dp[-1] + v)
        if w > t:
            continue
        dp[w:] = np.maximum(dp[:-w] + v, dp[w:])
    return np.max(candidates)

n, t = map(int, input().split())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())
print(solve(n, t, a, b))
