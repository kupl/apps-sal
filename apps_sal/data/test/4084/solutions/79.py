def answer(n: int, a: int, b: int) -> int:
    q, mod = divmod(n, a + b)
    return q * a + min(a, mod)


def main():
    n, a, b = list(map(int, input().split()))
    print((answer(n, a, b)))


def __starting_point():
    main()


__starting_point()
