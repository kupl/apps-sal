import numpy as np
n = int(input())
a = np.array(list(map(int, input().split())))
mod = 10 ** 9 + 7
ans = 0
two = 1
for i in range(61):
    one = np.count_nonzero(a & 1)
    a = a >> 1
    ans = (ans + one * (n - one) * two) % mod
    two = two * 2 % mod
print(ans)
