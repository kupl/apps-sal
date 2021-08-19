import numpy as np
n = int(input())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7
ans = 0
a = np.array(a)
for i in range(60):
    keta = a >> i & 1
    num1 = int(keta.sum())
    num0 = n - num1
    ans += 2 ** i % mod * (num1 * num0)
    ans %= mod
print(ans)
