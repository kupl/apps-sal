import numpy as np
(N, K) = [int(x) for x in input().split()]
A = np.array([int(x) for x in input().split()])
I = np.array([1] * N)
L = np.max(A)
ans = L
low = 1
high = L
while 1:
    if low == high:
        ans = low
        break
    mid = (low + high) // 2
    if np.sum((A - I) // mid) <= K:
        high = mid
    else:
        low = mid + 1
print(ans)
