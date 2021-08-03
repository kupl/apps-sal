
def __starting_point():
    x0, y0, ax, ay, bx, by = input().split()
    x0 = int(x0)
    y0 = int(y0)
    ax = int(ax)
    ay = int(ay)
    bx = int(bx)
    by = int(by)
    a = [(x0, y0)]
    n = 100
    x = x0
    y = y0
    for i in range(1, n):
        x = ax * x + bx
        y = ay * y + by
        a.append((x, y))
    xs, ys, t = input().split()
    xs = int(xs)
    ys = int(ys)
    t = int(t)
    ans = 0
    for i in range(n):
        if abs(xs - a[i][0]) + abs(ys - a[i][1]) > t:
            continue
        cur = 1
        T = t
        T -= abs(xs - a[i][0]) + abs(ys - a[i][1])
        for j in range(i + 1, n):
            if abs(a[j][0] - a[j - 1][0]) + abs(a[j][1] - a[j - 1][1]) > T:
                break
            cur += 1
            T -= abs(a[j][0] - a[j - 1][0]) + abs(a[j][1] - a[j - 1][1])
        ans = max(ans, cur)
        cur = 1
        T = t
        T -= abs(xs - a[i][0]) + abs(ys - a[i][1])
        for j in range(i - 1, -1, -1):
            if abs(a[j][0] - a[j + 1][0]) + abs(a[j][1] - a[j + 1][1]) > T:
                break
            cur += 1
            T -= abs(a[j][0] - a[j + 1][0]) + abs(a[j][1] - a[j + 1][1])
        ans = max(ans, cur)
    print(ans)


__starting_point()
