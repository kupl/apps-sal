n, a, ra, m = list(map(int, input().split()))
h = list(map(int, input().split()))
if a + ra < m:
    l, r = 0, 10 ** 9 + 1
    for _ in range(50):
        c1 = (l * 2 + r) // 3
        c2 = (l + r * 2) // 3
        p1 = 0
        p2 = 0
        q1 = 0
        q2 = 0
        for x in h:
            if c1 <= x:
                q1 += x - c1
            else:
                p1 += c1 - x
            if c2 <= x:
                q2 += x - c2
            else:
                p2 += c2 - x
        f1 = p1 * a + q1 * ra
        f2 = p2 * a + q2 * ra
        if f1 > f2:
            l = c1
        else:
            r = c2
    c1 = l + 1
    p1 = 0
    q1 = 0
    for x in h:
        if c1 <= x:
            q1 += x - c1
        else:
            p1 += c1 - x
    f1 = p1 * a + q1 * ra
    print(f1)
else:
    l, r = 0, 10 ** 9 + 1
    for _ in range(55):
        c1 = (l * 2 + r) // 3
        c2 = (l + r * 2) // 3
        p1 = 0
        p2 = 0
        q1 = 0
        q2 = 0
        for x in h:
            if c1 <= x:
                q1 += x - c1
            else:
                p1 += c1 - x
            if c2 <= x:
                q2 += x - c2
            else:
                p2 += c2 - x
        if p1 > q1:
            f1 = q1 * m + (p1 - q1) * a
        else:
            f1 = p1 * m + (q1 - p1) * ra
        if p2 > q2:
            f2 = q2 * m + (p2 - q2) * a
        else:
            f2 = p2 * m + (q2 - p2) * ra
        if f1 > f2:
            l = c1
        else:
            r = c2
    c1 = l + 1
    p1 = 0
    q1 = 0
    for x in h:
        if c1 <= x:
            q1 += x - c1
        else:
            p1 += c1 - x
    if p1 > q1:
        f1 = q1 * m + (p1 - q1) * a
    else:
        f1 = p1 * m + (q1 - p1) * ra
    print(f1)
