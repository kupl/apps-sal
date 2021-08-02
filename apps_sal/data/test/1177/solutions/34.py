import numpy as np
n, s = list(map(int, input().split()))
a = list(map(int, input().split()))
mod = 998244353
f = np.zeros(3001, int)

ans = 0
for ai in a:
    ff = np.zeros(3001, int)
    ff += f
    ff[ai:] += f[:-ai]
    ff[0] += 1
    ff[ai] += 1
    f = ff
    f %= mod
    ans += f[s]
    ans %= mod
print(ans)
