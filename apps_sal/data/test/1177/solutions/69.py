import numpy as np
mod = 998244353
N, S = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
coef = np.zeros(3001, dtype=int)
ans = 0
for a in A:
    coef[0] += 1
    coef[a:] += coef[:-a]
    coef %= mod
    ans += coef[S]
    ans %= mod
print(ans)
