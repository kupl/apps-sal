n = int(input())
rx = 0
ry = 0
rt = 0
ok = True
for _ in range(n):
    (t, x, y) = map(int, input().split())
    dist = abs(x - rx) + abs(y - ry)
    if dist <= abs(t - rt) and (abs(t - rt) - dist) % 2 == 0:
        rx = x
        ry = y
        rt = t
    else:
        ok = False
if ok:
    print('Yes')
else:
    print('No')
