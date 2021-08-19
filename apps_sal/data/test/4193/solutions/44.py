a = input()
a = a.split()
b = input()
b = b.split()
c = input()
c = c.split()
d = [a[0], b[0], c[0]]
e = [a[1], b[1], c[1]]
f = [a[2], b[2], c[2]]
g = [a[0], b[1], c[2]]
h = [a[2], b[1], c[0]]
n = int(input())
for i in range(n):
    j = int(input())
    for k in range(3):
        if int(a[k]) == j:
            a.pop(k)
            a.insert(k, 0)
        if int(b[k]) == j:
            b.pop(k)
            b.insert(k, 0)
        if int(c[k]) == j:
            c.pop(k)
            c.insert(k, 0)
        if int(d[k]) == j:
            d.pop(k)
            d.insert(k, 0)
        if int(e[k]) == j:
            e.pop(k)
            e.insert(k, 0)
        if int(f[k]) == j:
            f.pop(k)
            f.insert(k, 0)
        if int(g[k]) == j:
            g.pop(k)
            g.insert(k, 0)
        if int(h[k]) == j:
            h.pop(k)
            h.insert(k, 0)
if a == [0, 0, 0] or b == [0, 0, 0] or c == [0, 0, 0] or (d == [0, 0, 0]) or (e == [0, 0, 0]) or (f == [0, 0, 0]) or (g == [0, 0, 0]) or (h == [0, 0, 0]):
    print('Yes')
else:
    print('No')
