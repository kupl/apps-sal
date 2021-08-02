def answer(d: int, n: int) -> int:
    if n == 100:
        n += 1
    return 100 ** d * n


def main():
    d, n = map(int, input().split())
    print(answer(d, n))


def __starting_point():
    main()


__starting_point()
