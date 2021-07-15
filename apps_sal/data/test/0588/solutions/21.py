import math
n = int(input())
xy = []
for i in range(n):
    x, y = [int(item) for item in input().split()]
    if x == 0 and y == 0:
        rad = 0.0
    elif x == 0:
        if y > 0:
            rad = math.pi / 2.0
        elif y < 0:
            rad = -math.pi / 2.0
    else:
        rad = math.atan2(y, x)
    deg = math.degrees(rad)
    xy.append((deg, x, y))

xy.sort()
xy2 = xy[:]
for i, (d, x, y) in enumerate(xy):
    xy2.append((d+360.0, x, y))
    if i == 0:
        xy2.append((d+720.0, x, y))
xy2.sort()

ans = 0.0
for i in range(n):
    for j in range(i+1, i+n+1):
        x = 0.0; y = 0.0
        for k in range(i, j):
            x += xy2[k][1]
            y += xy2[k][2]
        d = math.hypot(x, y)
        ans = max(ans, d)

print(ans)
