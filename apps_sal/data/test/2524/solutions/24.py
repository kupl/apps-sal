import numpy as np
n = int(input())
tmp = list(map(int, input().split()))

mod = 10**9 + 7
a = np.array(tmp, np.int64)

ans = 0
for i in range(60 + 1):
    b = (a >> i) & 1
    iti = np.count_nonzero(b)
    zero = n - iti
    ans += (iti * zero) * pow(2, i, mod) % mod
ans %= mod
print(ans)
