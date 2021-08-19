import math
import bisect
import numpy as np
(N, k) = list(map(int, input().split()))
X = list(map(int, input().split()))
ans = float('inf')
for i in range(N - k + 1):
    a = X[i]
    b = X[i + k - 1]
    if np.sign(a) * np.sign(b) >= 0:
        ans = min(ans, max(abs(a), abs(b)))
    else:
        ans = min(ans, abs(a) + abs(b) + min(abs(a), abs(b)))
print(ans)
