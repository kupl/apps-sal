import numpy as np
(n, s) = map(int, input().split())
A = list(map(int, input().split()))
MOD = 998244353
U = 3010
count = 0
F = np.zeros(U + 1, np.int64)
for a in A:
    F[0] += 1
    F[a:] += F[:-a].copy()
    F %= MOD
    count += F[s]
count %= MOD
print(count)
