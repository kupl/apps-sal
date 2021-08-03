import numpy as np
n, m, x = map(int, input().split())
li = []
for i in range(n):
    c_A = list(map(int, input().split()))
    li.append(c_A)

li = np.array(li)
cost = 10**7
for i in range(2**n):
    c_s = np.array([0] * (m + 1))
    for j in range(n):
        if ((i >> j) & 1):
            c_s += li[j]
    if np.all(c_s[1:] >= x):
        cost = min(cost, c_s[0])
if cost == 10**7:
    print(-1)
else:
    print(cost)
