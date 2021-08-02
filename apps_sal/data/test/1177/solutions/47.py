from numpy import *
M = 998244353
N, S, *A = list(map(int, open(0).read().split()))
a = 0
f = zeros(S + 1, int)
for b in A:
    f[0] += 1
    f[b:] += f[:-b].copy()
    f %= M
    a += f[S]
print((a % M))
