import numpy as np
MOD = 1000000007
S = input()[::-1]
a = 10 ** np.arange(6) % 13
b = np.tile(np.arange(10), (6, 1))
c = a * b.T % 13
c = c.T
f = np.zeros((6, 13, 13), dtype=np.int64)
for i in range(6):
    f[i, 0, c[i]] = 1
    for j in range(12):
        f[i, j + 1] = np.roll(f[i, j], 1)
prev = np.zeros(13, dtype=np.int64)
prev[0] = 1
digit = 0
for (i, c) in enumerate(S):
    k = i % 6
    if c == '?':
        cur = np.dot(prev, f[k]) % MOD
        (prev, cur) = (cur, prev)
    else:
        digit += a[k] * (ord(c) - ord('0'))
m = (5 - digit) % 13
print(prev[m])
