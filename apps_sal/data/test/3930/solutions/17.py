(n, k) = map(int, input().split())
a = list(map(int, input().split()))
p = a[:]
for i in range(1, n):
    p[i] += p[i - 1]
z = 1
o = 0
r = 50
if k == -1:
    r = 2
elif k == 1:
    r = 1
for i in range(r):
    d = {}
    for j in range(n):
        if p[j] not in d:
            d[p[j]] = 0
        d[p[j]] += 1
        if p[j] - z in d:
            o += d[p[j] - z]
        if p[j] - z == 0:
            o += 1
    z *= k
print(o)
