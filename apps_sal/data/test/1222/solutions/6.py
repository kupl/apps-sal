
def solver(d, v, a):
    a.append(v)
    if d == 10:
        return

    for i in range(-1, 2):
        add = (v % 10) + i
        if add < 0 or 9 < add:
            continue
        solver(d + 1, v * 10 + add, a)


def main():
    k = int(input())

    a = []
    for i in range(1, 10):
        solver(1, i, a)
    a.sort()

    print((a[k - 1]))


def __starting_point():
    main()


__starting_point()
