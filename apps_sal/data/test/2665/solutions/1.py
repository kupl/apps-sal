def chefsqua():
    import sys

    def gcd(a, b):
        while b > 0:
            (a, b) = (b, a % b)
        return a
    n = int(sys.stdin.readline().strip())
    coords = []
    cset = set()
    (orgx, orgy) = (0, 0)
    (basex, basey) = (1, 1)
    colinear = True
    for i in range(n):
        (x, y) = tuple(map(int, sys.stdin.readline().strip().split(' ')))
        if i == 0:
            (orgx, orgy) = (x, y)
        (x, y) = (x - orgx, y - orgy)
        coords.append((x, y))
        cset.add((x, y))
        if i == 1:
            g = gcd(x, y)
            (basex, basey) = (x // g, y // g)
        if colinear and i >= 2:
            g = gcd(x, y)
            colinear &= x // g == basex and y // g == basey
    if n == 0:
        print(4)
        return
    if n == 1:
        print(3)
        return
    elif n == 2 or colinear:
        print(2)
        return
    best = 2
    for i in range(n - 1):
        (xi, yi) = (coords[i][0], coords[i][1])
        for j in range(i + 1, n):
            (xj, yj) = (coords[j][0], coords[j][1])
            (dx, dy) = (xj - xi, yj - yi)
            if (xi - dy, yi + dx) in cset:
                best = 1
                if (xj - dy, yj + dx) in cset:
                    print(0)
                    return
            if (xi + dy, yi - dx) in cset:
                best = 1
                if (xj + dy, yj - dx) in cset:
                    print(0)
                    return
            if (xj - dy, yj + dx) in cset:
                best = 1
            if (xj + dy, yj - dx) in cset:
                best = 1
    print(best)
    return


chefsqua()
