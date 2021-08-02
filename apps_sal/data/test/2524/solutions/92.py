import numpy as np
n = int(input())
mod = 10**9 + 7
a = np.array(list(map(int, input().split())))
ans = 0
for i in range(len(bin(max(a)))):
    num_1 = np.count_nonzero((a >> i) & 1)
    num_0 = n - num_1
    ans += (2**i) * (num_1 * num_0) % mod
ans %= mod
print(ans)
