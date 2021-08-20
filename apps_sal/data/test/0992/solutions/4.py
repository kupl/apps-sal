import numpy as np
(N, S) = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
mod = 998244353
coef = np.zeros(3001, dtype=int)
coef[0] = 1
for a in A:
    coef2 = coef[:-a].copy()
    coef *= 2
    coef[a:] += coef2
    coef %= mod
print(coef[S])
