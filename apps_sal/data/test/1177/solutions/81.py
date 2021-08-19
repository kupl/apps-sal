import numpy as np
(n, s) = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
mod = 998244353
f = np.zeros(s + 1, int)
for i in a:
    f[0] += 1
    f[i:] += f[:-i].copy()
    f %= mod
    ans += f[s]
print(ans % mod)
