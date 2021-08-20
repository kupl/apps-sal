import numpy as np
(n, s) = map(int, input().split())
a = list(map(int, input().split()))
mod = 998244353
f = np.zeros(3020, np.int64)
f[0] = 1
for b in a:
    ff = 2 * f
    ff[b:] += f[:-b]
    ff %= mod
    f = ff
print(f[s])
