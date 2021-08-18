import numpy as np
N, T = map(int, input().split())

meals = [tuple(map(int, input().split())) for _ in range(N)]


dp1 = np.zeros(T, dtype=int)
dp2 = np.zeros(T, dtype=int)

for a, b in meals:
    ndp1 = dp1.copy()
    ndp1[a:] = np.maximum(dp1[a:], dp1[:-a] + b)

    ndp2 = dp2.copy()
    ndp2[a:] = np.maximum(dp2[a:], dp2[:-a] + b)
    ndp2 = np.maximum(ndp2, dp1 + b)
    dp1, dp2 = ndp1, ndp2

print(ndp2[-1])
