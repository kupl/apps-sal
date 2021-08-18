import numpy as np

a = [list(map(int, input().split())) for i in range(3)]
n = int(input())

for i in range(n):
    b = int(input())

    for j in range(3):
        if b in a[j]:
            idx = a[j].index(b)
            a[j][idx] = 0

np_a = np.array(a)
np_t = np_a.T
d = 0
u = 0

for i in range(3):
    r = np_a[i]
    c = np_t[i]
    d += r[i]
    u += r[2 - i]

    if r.sum() and c.sum():
        continue

    print("Yes")
    return


if d and u:
    print("No")
else:
    print("Yes")
