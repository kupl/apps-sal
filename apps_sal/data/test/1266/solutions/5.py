n = int(input())
(x0, y0) = [int(x) for x in input().split()]
uv = [-1, -10 ** 10, 'n']
dv = [-1, 10 ** 10, 'n']
lh = [-10 ** 10, -1, 'n']
rh = [10 ** 10, -1, 'n']
ldd = [-10 ** 10, -1, 'n']
lud = [-10 ** 10, -1, 'n']
rdd = [10 ** 10, -1, 'n']
rud = [10 ** 10, -1, 'n']
for i in range(n):
    (t, x, y) = [x for x in input().split()]
    x = int(x)
    y = int(y)
    if x == x0:
        if y < y0:
            if y0 - y < y0 - uv[1]:
                uv = [x, y, t]
        elif y - y0 < dv[1] - y0:
            dv = [x, y, t]
    if y == y0:
        if x < x0:
            if x0 - x < x0 - lh[0]:
                lh = [x, y, t]
        elif x - x0 < rh[0] - x0:
            rh = [x, y, t]
    if abs(x - x0) == abs(y - y0):
        if x < x0 and y < y0:
            if x0 - x < x0 - ldd[0]:
                ldd = [x, y, t]
        if x < x0 and y > y0:
            if x0 - x < x0 - lud[0]:
                lud = [x, y, t]
        if x > x0 and y < y0:
            if x - x0 < rdd[0] - x0:
                rdd = [x, y, t]
        if x > x0 and y > y0:
            if x - x0 < rud[0] - x0:
                rud = [x, y, t]
ans = 'NO'
if uv[2] in ('R', 'Q') or dv[2] in ('R', 'Q') or lh[2] in ('R', 'Q') or (rh[2] in ('R', 'Q')):
    ans = 'YES'
if ldd[2] in ('B', 'Q') or lud[2] in ('B', 'Q') or rdd[2] in ('B', 'Q') or (rud[2] in ('B', 'Q')):
    ans = 'YES'
print(ans)
