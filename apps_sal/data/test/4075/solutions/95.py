import numpy as np
n, m = list(map(int, input().split()))
s = [[0] * 10 for _ in range(m)]
for i in range(m):
    k = list(map(int, input().split()))
    for j in range(1, k[0] + 1):
        s[i][10 - k[j]] = 1
s = np.asarray(s)
p = list(map(int, input().split()))
ans = 0
for i in range(2**n):
    binst = format(i, '010b')
    l = list(map(int, list(binst)))
    l = np.asarray(l)
    on = s & l
    onsum = np.sum(on, axis=1) % 2
    err = 0
    for j in range(m):
        if onsum[j] != p[j]:
            err = 1
            break
    if err == 0:
        ans += 1
print(ans)
