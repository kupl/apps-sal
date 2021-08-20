n = int(input())
a = []
b = []
for q in range(n):
    (x, y) = map(int, input().split())
    a.append(x)
    b.append(y)
c = a[:]
d = b[:]
cc = a[:]
dd = b[:]
c.sort()
d.sort()
e = []
f = []
for k in range(1, n):
    e.append(d[k])
ind = b.index(d[0])
del cc[ind]
for k in range(n - 1):
    f.append(cc[k])
f.sort()
i1 = e[0] - f[-1]
g = []
h = []
for k in range(n - 1):
    g.append(c[k])
ind2 = a.index(c[-1])
del dd[ind2]
for k in range(n - 1):
    h.append(dd[k])
h.sort()
i2 = h[0] - g[-1]
ww = max(i1, i2)
if ww < 0:
    print(0)
else:
    print(ww)
