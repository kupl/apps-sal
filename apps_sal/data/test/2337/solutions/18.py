def main():
    (n, m) = map(int, input().split())
    aa = list(map(int, input().split()))
    it = iter(list(map(int, input().split())))
    try:
        for (i, a) in enumerate(aa, 1):
            b = next(it)
            while b < a:
                b = next(it)
    except StopIteration:
        i -= 1
    print(n - i)


def __starting_point():
    main()


__starting_point()
