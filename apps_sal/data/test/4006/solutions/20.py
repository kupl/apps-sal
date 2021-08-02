def f(x):
    return int(str(x + 1).rstrip('0'))


def main():
    x = int(input())

    l = set()

    while x not in l:
        l.add(x)
        x = f(x)

    print(len(l))


def __starting_point():
    main()


__starting_point()
