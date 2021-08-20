import numpy as np
mod = 10 ** 9 + 7
n = int(input())
A = np.array(list(map(int, input().split())))
ans = 0
for i in range(60):
    n1 = np.count_nonzero(A >> i & 1)
    n0 = n - n1
    ans += 2 ** i * n1 * n0 % mod
ans %= mod
print(ans)
