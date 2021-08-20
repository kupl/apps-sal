def main():
    (n, m) = list(map(int, input().split()))
    (xx, yy, walls, t) = ([0] * n, [0] * m, set(), n + m)
    for x in range(n):
        for (y, c) in enumerate(input()):
            if c == '*':
                walls.add((x, y))
                if len(walls) == t:
                    print('NO')
                    return
                xx[x] += 1
                yy[y] += 1
    for (x, a) in enumerate(xx):
        t = len(walls) - a
        for (y, b) in enumerate(yy):
            if b - ((x, y) in walls) == t:
                print('YES')
                print(x + 1, y + 1)
                return
    print('NO')


def __starting_point():
    main()


__starting_point()
