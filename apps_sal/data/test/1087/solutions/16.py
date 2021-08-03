n, k, *a = map(int, open(0).read().split())
d = [0] * 41
for i in range(n):
    for j in range(41):
        d[j] += (a[i] >> j) & 1
f = 0
la = len(bin(max(a))) - 2
lk = len(bin(k)) - 2
b = [0] * 41
for i in range(lk - 1, -1, -1):
    if (k >> i) & 1 == 1:
        if d[i] < n - d[i]:
            b[i] = 1
        else:
            b[i] = 0
            f = 1
    if (k >> i) & 1 == 0:
        if d[i] < n - d[i] and f == 1:
            b[i] = 1
        else:
            b[i] = 0
ans = 0
for i in range(max(lk, la)):
    ans += (1 << i) * [d[i], n - d[i]][b[i]]
print(ans)
