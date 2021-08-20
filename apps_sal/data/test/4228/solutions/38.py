import numpy as np
(N, L) = list(map(int, input().split()))
taste = np.arange(1, N + 1) + L - 1
min_ind = np.argmin(np.abs(taste))
mask_1 = np.ones(N, dtype=bool)
mask_1[min_ind] = False
ans = np.sum(taste[mask_1])
print(ans)
