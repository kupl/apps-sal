(n, m) = list(map(int, input().split()))
a = []
b = []
y = -1
for i in range(m):
    a.append(list(map(int, input().split())))
    b.append(set(a[-1]))
    if i >= 1 and y == -1:
        if not b[0] & b[-1]:
            y = i
if m <= 2 or y == -1:
    print('YES')
else:
    (c, d, e, f) = (*a[0], *a[y])
    x = [{c, e}, {c, f}, {d, e}, {d, f}]
    z = [True, True, True, True]
    for pair in b:
        for zp in [0, 1, 2, 3]:
            z[zp] = z[zp] if pair & x[zp] else False
    if z[0] or z[1] or z[2] or z[3]:
        print('YES')
    else:
        print('NO')
