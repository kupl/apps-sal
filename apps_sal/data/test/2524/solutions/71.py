import numpy as np


n = int(input())
a = list(map(int, input().split()))

a = np.array(a, dtype='int64')
MOD = 10**9 + 7
ans = 0
for i in range(60):
    ca = a >> i & 1
    c1 = int(ca.sum())
    c0 = n - c1
    c0c1 = (c0 * c1) % MOD
    c0c1pow = (c0c1 * 2**i) % MOD
    ans = (ans + c0c1pow) % MOD
print(ans)
