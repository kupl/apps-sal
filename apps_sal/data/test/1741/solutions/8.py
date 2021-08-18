import math

n = int(input())
points = []
npt = 0
for i in range(n):
    point = list(map(int, input().split()))
    if point[1] < 0:
        npt += 1
        point[1] = -point[1]
    points.append(point)
if npt < n and npt > 0:
    print(-1)
else:
    l, r = 0, 1e16
    count = 100
    while abs(r - l) > 1e-6 and count > 0:
        count -= 1
        ok = True
        mid = (l + r) / 2
        a, b = -float('inf'), float('inf')
        for i in range(n):
            x, y = points[i]
            if y > 2 * mid:
                l = mid
                ok = False
                break
            delta = math.sqrt(y * (2 * mid - y))
            a, b = max(a, x - delta), min(b, x + delta)
        if not ok:
            continue
        if a > b:
            l = mid
        else:
            r = mid
    print((l + r) / 2)
