def main():
    n, m = list(map(int, input().split()))
    xx, yy, walls, t = [0] * n, [0] * m, set(), 0
    for x in range(n):
        for y, c in enumerate(input()):
            if c == '*':
                t += 1
                if t == n + m:
                    print("NO")
                    return
                walls.add((x, y))
                xx[x] += 1
                yy[y] += 1
    for x, a in enumerate(xx):
        for y, b in enumerate(yy):
            if a + b - ((x, y) in walls) == t:
                print("YES")
                print(x + 1, y + 1)
                return
    print("NO")


def __starting_point():
    main()


__starting_point()
