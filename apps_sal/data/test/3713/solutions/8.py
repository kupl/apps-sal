def main():
    n, t, a = int(input()), 0, '*'
    for b in input():
        if a == b:
            t += 1
        else:
            a = b
    print(n - max(t - 2, 0))


def __starting_point():
    main()

__starting_point()
