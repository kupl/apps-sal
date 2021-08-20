import numpy as np
(N, S) = list(map(int, input().split()))
A = list(map(int, input().split()))
mod = 998244353
f = np.zeros(3100, np.int64)
ans = 0
f[0] = 1
for a in A:
    g = f.copy()
    f[a:] += g[:-a]
    f += g
    f %= mod
print(f[S])
