def main():
    input()
    x = m = float(input())
    try:
        for s in input(), input():
            for a in map(float, s.split()):
                x *= a / (a - 1.)
        print(x - m)
    except ZeroDivisionError:
        print(-1)


def __starting_point():
    main()


__starting_point()
