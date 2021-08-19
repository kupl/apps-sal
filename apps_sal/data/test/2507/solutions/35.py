import numpy as np
(N, K) = map(int, input().split())
A = [int(c) for c in input().split()]
F = [int(c) for c in input().split()]
A.sort()
F.sort(reverse=True)
A = np.array(A)
F = np.array(F)
Asum = A.sum()
M = np.max(A * F)
l = -1
r = M + 1
while l + 1 < r:
    s = (l + r) // 2
    cnt = Asum - np.minimum(A, s // F).sum()
    if cnt > K:
        l = s
    else:
        r = s
print(r)
