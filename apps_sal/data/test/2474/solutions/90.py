import numpy as np
MOD = 10**9 + 7


def plu(a, b):
    return (a + b) % MOD


plus = np.frompyfunc(plu, 2, 1)

n = int(input())
c = np.sort(np.array(input().split(), dtype=np.int64))
p = pow(2, 2 * n - 2, MOD)
print((plus.reduce(np.mod(np.mod(p * c, MOD) * (n - np.arange(n) + 1), MOD))))
