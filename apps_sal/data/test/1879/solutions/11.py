def main():
    t, x, y, ex, ey = list(map(int, input().split()))
    x -= ex
    y -= ey
    for i, c in enumerate(input()):
        if x == 0 == y:
            print(i)
            return
        if c == 'E':
            if x < 0:
                x += 1
        elif c == 'W':
            if x > 0:
                x -= 1
        elif c == 'N':
            if y < 0:
                y += 1
        elif c == 'S':
            if y > 0:
                y -= 1
    print(t if x == 0 == y else -1)


def __starting_point():
    main()

__starting_point()
