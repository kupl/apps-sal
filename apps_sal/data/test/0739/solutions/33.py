import numpy as np
(l, a, b, m) = list(map(int, input().split()))
s_max = a + b * (l - 1)
ten_pow = [1]
while ten_pow[-1] <= s_max:
    ten_pow.append(ten_pow[-1] * 10)
D_MAX = len(ten_pow)
d = [0] * D_MAX
for i in range(D_MAX):
    if ten_pow[i] >= a:
        d[i] = max((ten_pow[i] - 1 - a) // b, 0)
d[-1] = l - 1
cd = [d[i + 1] - d[i] for i in range(len(d) - 1)]
y = np.array([a, a + b, 1]).T % m
for i in range(len(cd)):
    x = np.array([[ten_pow[i + 1] % m, 1, 0], [0, 1, b], [0, 0, 1]])
    x %= m
    k = cd[i]
    while k > 0:
        if k & 1:
            y = np.dot(x, y) % m
        x = np.dot(x, x) % m
        k = k >> 1
ans = y[0] % m
print(ans)
