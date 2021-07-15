import numpy as np
n = int(input())
a = np.array(list(map(int, input().split())))

bit = [0] * 60
mod = 10 ** 9 + 7
ans = 0
for i in range(60):
    n1 = np.count_nonzero((a >> i) & 1)
    n0 = n - n1
    ans += (2 ** i) * n1 * n0 % mod
print(ans % mod)
