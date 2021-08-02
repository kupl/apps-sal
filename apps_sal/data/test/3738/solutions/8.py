def main():
    a, b = list(map(int, input().split()))
    steps, t = [((-1, 1, 0)["LR".find(c)], (-1, 1, 0)["DU".find(c)]) for c in input()], -25
    x = sum(e[0] for e in steps)
    y = sum(e[1] for e in steps)
    if x and y:
        t += min(a // x, b // y)
    elif x:
        t += a // x
    elif y:
        t += b // y
    if t > 0:
        a -= t * x
        b -= t * y
    for _ in range(26):
        for dx, dy in steps:
            if not (a or b):
                print("Yes")
                return
            a -= dx
            b -= dy
    print("No")


def __starting_point():
    main()


__starting_point()
