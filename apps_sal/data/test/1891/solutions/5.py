def explosion(a, x, y, q, l, r):
    if r - l == 1:
        q1 = q
        while q1 < len(a) and a[q1] < r:
            q1 += 1
        if q1 == q:
            return x
        else:
            return (q1 - q) * y
    q1 = q
    while q1 < len(a) and a[q1] < (l + r) // 2:
        q1 += 1
    q2 = q1
    while q2 < len(a) and a[q2] < r:
        q2 += 1
    if q1 - q == 0 and q2 - q1 == 0:
        return x
    if q2 - q1 != 0 and q1 - q != 0:
        (d1, d2, d) = (explosion(a, x, y, q, l, (l + r) // 2), explosion(a, x, y, q1, (l + r) // 2, r), (q2 - q) * (r - l) * y)
        if d1 + d2 < d:
            return d1 + d2
        else:
            return d
    if q1 != q:
        (d, d1) = (explosion(a, x, y, q, l, (l + r) // 2), (r - l) * (q1 - q) * y)
        if x + d < d1:
            return x + d
        else:
            return d1
    else:
        (d, d1) = (explosion(a, x, y, q1, (l + r) // 2, r), (r - l) * (q2 - q1) * y)
        if x + d < d1:
            return x + d
        else:
            return d1


(n, k, x, y) = list(map(int, input().split()))
a = sorted(list([int(x) - 1 for x in input().split()]))
print(explosion(a, x, y, 0, 0, 2 ** n))
