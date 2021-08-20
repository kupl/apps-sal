n = int(input())
m = [0] * 366
f = [0] * 366
res = 0
for i in range(n):
    (x, l, r) = [i for i in input().split()]
    l = int(l)
    r = int(r)
    if x == 'M':
        for j in range(l - 1, r):
            m[j] += 1
    else:
        for j in range(l - 1, r):
            f[j] += 1
for i in range(366):
    res = max(res, min(m[i], f[i]))
print(res * 2)
