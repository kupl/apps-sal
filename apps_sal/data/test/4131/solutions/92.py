(n, m) = map(int, input().split())
a = []
for i in range(m):
    (x, y) = map(int, input().split())
    a.append([x, y])
b = a.copy()
c = sorted(b, key=lambda x: (x[0], x[1]))
d = [{} for i in range(10 ** 5 + 1)]
count = 1
s = '%d' % c[0][0]
s = s.zfill(6)
s2 = '%d' % count
s2 = s2.zfill(6)
d1 = {c[0][1]: s + s2}
for i in range(1, m):
    if c[i][0] == c[i - 1][0]:
        count += 1
        s2 = '%d' % count
        s2 = s2.zfill(6)
        d1[c[i][1]] = s + s2
    else:
        d[c[i - 1][0]] = d1
        count = 1
        s = '%d' % c[i][0]
        s = s.zfill(6)
        s2 = '%d' % count
        s2 = s2.zfill(6)
        d1 = {c[i][1]: s + s2}
d[c[-1][0]] = d1
for i in range(m):
    d2 = d[a[i][0]]
    print(d2.get(a[i][1]))
