def f():
    return input().split()


(n, m, k) = map(int, f())
c = {x: ([x], []) for x in f()}
for i in range(m):
    (t, x, y) = f()
    s = 2 - int(t)
    (cx, cy) = (c[x], c[y])
    if cx[0] is cy[s]:
        print('NO')
        continue
    print('YES')
    if cx[0] is cy[1 - s]:
        continue
    if len(cx[0]) + len(cx[1]) < len(cy[0]) + len(cy[1]):
        (cx, cy) = (cy, cx)
    (ux, vx) = cx
    if s:
        (uy, vy) = cy
    else:
        (vy, uy) = cy
    ux += uy
    vx += vy
    for x in uy:
        c[x] = (ux, vx)
    for x in vy:
        c[x] = (vx, ux)
for i in range(k):
    (x, y) = f()
    print(1 if c[x][0] is c[y][0] else 2 if c[x][0] is c[y][1] else 3)
