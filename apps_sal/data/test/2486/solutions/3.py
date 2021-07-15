import numpy as np
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
dp1 = np.zeros((N+1, K), dtype=bool)
dp1[0][0] = 1
for i, a in enumerate(A, 1):
    dp1[i, :] = dp1[i-1, :]
    dp1[i, a:] += dp1[i-1, :-a]
dp2 = np.zeros((N+1, K), dtype=bool)
dp2[N][0] = 1
for i, a in zip(list(range(N-1, -1, -1)), A[::-1]):
    dp2[i, :] = dp2[i+1, :]
    dp2[i, a:] += dp2[i+1, :-a]
ans = 0
for a, d1, d2 in zip(A, dp1[:-1], dp2[1:]):
    if a >= K:
        continue
    d2_ = np.zeros(K+a, dtype=np.int32)
    d2_[a:] = d2
    d2_cum = np.cumsum(d2_)
    d2_diff = d2_cum[a:] - d2_cum[:-a]
    d = d2_diff[::-1] * d1
    if (d == 0).all():
        ans += 1
print(ans)

