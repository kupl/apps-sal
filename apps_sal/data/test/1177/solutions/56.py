import numpy as np
(N, S) = map(int, input().split())
x = [int(x) for x in input().split()]
m = np.zeros((S + 1, 3))
p = np.zeros((S + 1, 3))
p[0, 0] = 1
for i in range(1, N + 1):
    m[:, 0] = p[:, 0]
    m[:, 1] = p[:, 0] + p[:, 1]
    m[:, 2] = p[:, 0] + p[:, 1] + p[:, 2]
    m[x[i - 1]:, 1] += p[:-x[i - 1], 0] + p[:-x[i - 1], 1]
    m[x[i - 1]:, 2] += p[:-x[i - 1], 0] + p[:-x[i - 1], 1]
    p[:, 0] = m[:, 0] % 998244353
    p[:, 1] = m[:, 1] % 998244353
    p[:, 2] = m[:, 2] % 998244353
print(int(p[S, 2]))
