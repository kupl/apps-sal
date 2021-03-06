def scan():
    return list(map(int, input().split()))


(x1, y1, x2, y2) = scan()
(vmx, t) = scan()
(vx, vy) = scan()
(wx, wy) = scan()
(lb, ub, EPS) = (0, 1000000000000000.0, 1e-08)
while ub - lb > EPS:
    mid = (lb + ub) / 2
    (xx, yy) = (vx * mid, vy * mid) if t - mid > EPS else (vx * t + wx * (mid - t), vy * t + wy * (mid - t))
    if vmx * mid - ((x2 - x1 - xx) ** 2 + (y2 - y1 - yy) ** 2) ** 0.5 > EPS:
        ub = mid
    else:
        lb = mid
print('%.8f' % ub)
