import numpy as np

N = int(input())
mod = 10**9 + 7
A = np.array(input().split(), int)

ans = 0
for i in range(60):
    b = np.count_nonzero(A >> i & 1)
    ans += 2**i*(b*(N-b))
    ans %= mod
    c = np.count_nonzero(A >> i & 1)
print(ans)


