import numpy as np
N, K = list(map(int, input().split()))
MOD = 10**9 + 7
div = list(range(1, int(np.sqrt(N)) + 1))
L1 = len(div)
div2 = [N // val for val in div]
div2.sort()
if div[-1] == div2[0]:
    div2.remove(div2[0])
L2 = len(div2)
L = L1 + L2
ls = [1] * L1 + [0] * L2
tmp = div[-1]
for i, val in enumerate(div2):
    ls[i + L1] = val - tmp
    tmp = val
dp = [0] * L
dp = np.zeros((L), dtype='int64')
ls = np.array(ls, dtype='int64')
dp[:] = ls
r = np.zeros(L + 1, dtype='int64')
r[:-1] = np.cumsum(dp, dtype='int64')[::-1]
for i in range(K - 1):
    dp = (r[:-1] * ls) % MOD
    r[:-1] = np.cumsum(dp, dtype='int64')[::-1]
print((r[0] % MOD))
