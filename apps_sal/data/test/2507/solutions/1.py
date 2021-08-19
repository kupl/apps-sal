import numpy as np
(n, k) = map(int, input().split())
a = [int(x) for x in input().split()]
f = [int(x) for x in input().split()]
a.sort()
f.sort(reverse=True)
A = np.array(a)
F = np.array(f)
S = sum(a)
(l, u) = (-1, f[0] * a[-1])
while l + 1 < u:
    m = (l + u) // 2
    s = 0
    if S - np.minimum(A, m // F).sum() <= k:
        u = m
    else:
        l = m
print(u)
