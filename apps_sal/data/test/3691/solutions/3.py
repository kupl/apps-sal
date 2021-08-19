import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
(x0, y0, ax, ay, bx, by) = list(map(int, input().split()))
(xs, ys, t) = list(map(int, input().split()))
p = [(x0, y0)]
d = [0]
m = 100
for i in range(m):
    (x, y) = p[-1]
    nx = ax * x + bx
    ny = ay * y + by
    nd = abs(nx - x) + abs(ny - y)
    d.append(d[-1] + nd)
    p.append((nx, ny))
ans = 0
for i in range(m):
    (x, y) = p[i]
    init_d = abs(x - xs) + abs(y - ys)
    if init_d > t:
        continue
    tmp = 1
    rem = t - init_d
    left = -1
    right = i
    while right - left > 1:
        mid = (right + left) // 2
        if d[i] - d[mid] <= rem:
            right = mid
        else:
            left = mid
    tmp += i - right
    ans = max(ans, tmp)
    tmp = 1
    left = i
    right = m
    while right - left > 1:
        mid = (right + left) // 2
        if d[mid] - d[i] <= rem:
            left = mid
        else:
            right = mid
    tmp += left - i
    ans = max(ans, tmp)
print(ans)
