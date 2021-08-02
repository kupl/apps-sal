def main():
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    delim = 0

    for i, e in enumerate(a):
        e += delim
        p, delim = divmod(e, m)
        print(p, end=' ')

    print()


def __starting_point():
    main()


__starting_point()
