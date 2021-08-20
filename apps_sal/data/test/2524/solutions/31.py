import numpy as np
mod = 10 ** 9 + 7
ans = 0
N = int(input())
A = list(map(int, input().split()))
A_np = np.array(A, dtype=np.int64)
for i in range(60):
    c = np.count_nonzero(A_np & 1)
    ans += 2 ** i * c * (N - c)
    A_np >>= 1
print(ans % mod)
