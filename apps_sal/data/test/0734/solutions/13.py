import math
(n, m) = map(int, input().split())
a = sorted(list(map(int, input().split())))
res = 0
nr = 1
f = 1
for i in range(len(a) - 1):
    if a[i] != 0:
        if a[i] == 1:
            nr = 2
            continue
        if nr > a[i]:
            res += max(0, max(0, nr - 1) - 1)
        else:
            res += max(0, a[i] - nr) + max(0, nr - 1)
        if a[i] - nr >= 0:
            f = 0
        if f == 0:
            nr += 1
            f = 1
if nr > a[-1]:
    res += max(0, max(0, nr - 1) - 1)
else:
    res += max(0, nr - 1)
print(res)
