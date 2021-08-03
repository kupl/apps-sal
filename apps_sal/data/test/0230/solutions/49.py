import numpy as np

n = int(input())
s = np.array(list(input()))

l = s.size

dp = np.zeros(l, dtype=np.int16)
ans = 0
for i, e in enumerate(s, 1):
    dp_prev = dp.copy()
    mx = np.arange(1, l + 1) - i
    idx = np.hstack([np.full(i, False), s[i:] == e]).astype(np.bool)
    idx_prev = np.roll(idx, -1)
    dp = np.zeros(l, dtype=np.int16)
    dp[idx] = np.minimum(dp_prev[idx_prev] + 1, mx[idx])
    ans = max(ans, dp.max())

print(ans)
