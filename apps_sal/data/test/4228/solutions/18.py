def answer(n: int, l: int) -> int:
    apples_taste = list(range(l, l + n))
    applepie_taste = sum(apples_taste) - min(apples_taste, key=abs)

    return applepie_taste


def main():
    n, l = list(map(int, input().split()))
    print((answer(n, l)))


def __starting_point():
    main()


__starting_point()
