def main():
    from collections import Counter
    n, *a = list(map(int, open(0).read().split()))
    s = len(set(a))

    if s % 2 == 1:
        print(s)
    else:
        print((s - 1))


def __starting_point():
    main()


__starting_point()
