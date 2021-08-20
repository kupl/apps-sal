from collections import defaultdict
import numpy as np
(N, K) = list(map(int, input().split()))
A = [0] + list(map(int, input().split()))
A = np.array(A)
A %= K
A = A.cumsum()
tmp = np.arange(N + 1)
B = (A - tmp) % K
ans = 0
d = defaultdict(int)
for i in range(min(K, N + 1)):
    x = B[i]
    ans += d[x]
    d[x] += 1
if N > K:
    for i in range(K, N + 1):
        x = B[i]
        y = B[i - K]
        d[y] -= 1
        ans += d[x]
        d[x] += 1
print(ans)
