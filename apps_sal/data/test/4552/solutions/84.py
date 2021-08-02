import numpy as np
n = int(input())
f = []
for i in range(n):
    f.append(list(map(int, input().split())))
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
x = np.asarray(f)
mx = -10**9
for i in range(1, 2**10):
    y = np.asarray([int(x) for x in list(format(i, '010b'))])
    z = x * y
    can = np.sum(z, axis=1)
    c = 0
    for j in range(n):
        c += p[j][can[j]]
    mx = max(c, mx)
print(mx)
