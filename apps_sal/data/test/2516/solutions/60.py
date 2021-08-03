import numpy as np
n, p = map(int, input().split())
s = [int(j) for j in input()][::-1]

if p == 2:
    ans = 0
    for i, j in enumerate(s):
        if j % 2 == 0:
            ans += (n - i)
    print(ans)
    return
if p == 5:
    ans = 0
    for i, j in enumerate(s):
        if j % 5 == 0:
            ans += (n - i)
    print(ans)
    return

c = [0] * p
tmp = 0
c[0] += 1
t = 1
for i in s:
    tmp += t * i
    c[tmp % p] += 1
    t = (t * 10) % p
c = np.array(c)
ans = c * (c - 1) // 2
print(ans.sum())
