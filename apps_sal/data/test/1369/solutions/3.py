def solve():
    from sys import stdin
    f_i = stdin

    N = int(f_i.readline())

    points = []
    for i in range(N):
        x, y = map(int, f_i.readline().split())
        points.append(x + y * 1j)

    from itertools import combinations
    radiuses = []

    for p1, p2 in combinations(points, 2):
        c = (p1 + p2) / 2
        r = abs(p1 - c)
        for p in points:
            if abs(p - c) > r:
                break
        else:
            radiuses.append(r)

    if radiuses:
        return min(radiuses)

    def circumcircle(a, b, c):
        n = (a - b) * abs(c) ** 2 + (b - c) * abs(a) ** 2 + (c - a) * abs(b) ** 2
        d = (a - b) * c.conjugate() + (b - c) * a.conjugate() + (c - a) * b.conjugate()
        return n / d  # center of circumcircle

    err = 10 ** -7
    for p1, p2, p3 in combinations(points, 3):
        z1 = p3 - p1
        z2 = p2 - p1
        if z1.real * z2.imag == z1.imag * z2.real:
            continue

        c = circumcircle(p1, p2, p3)
        r = abs(p1 - c)
        for p in points:
            # if abs(p - c) > r:
            if abs(p - c) - r > err:
                break
        else:
            radiuses.append(r)

    return min(radiuses)


print(solve())
