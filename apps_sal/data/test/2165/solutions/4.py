n, nt = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))
c = 0
ans = 0
l = []
r = []
for i in range(n):
    if t[i] < nt:
        l.append([nt - t[i], a[i]])
    if t[i] > nt:
        r.append([t[i] - nt, a[i]])
    if t[i] == nt:
        ans += a[i]
l = sorted(l, key=lambda x: x[0])
r = sorted(r, key=lambda x: x[0])
il = 0
ir = 0
lv = 0.0
rv = 0.0
lvv = 0.0
rvv = 0.0
while 1:
    if lv <= rv:
        if il ==len(l):
            break
        lv += l[il][0] * l[il][1]
        lvv += l[il][1]
        il += 1
    else:
        if ir ==len(r):
            break
        rv += r[ir][0] * r[ir][1]
        rvv += r[ir][1]
        ir += 1
if rv < lv:
    lv -= l[il - 1][0] * l[il - 1][1]
    lvv -= l[il - 1][1]
    lvv += (rv - lv) / l[il - 1][0]
elif lv < rv:
    rv -= r[ir - 1][0] * r[ir - 1][1]
    rvv -= r[ir - 1][1]
    rvv += (lv - rv) / r[ir - 1][0]

ans += rvv
ans += lvv
print("%.8f" % ans)
