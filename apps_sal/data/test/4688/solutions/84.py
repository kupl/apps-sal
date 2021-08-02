def answer(n: int, k: int) -> int:
    return k * (k - 1) ** (n - 1)


def main():
    n, k = map(int, input().split())
    print(answer(n, k))


def __starting_point():
    main()


__starting_point()
