def answer(n: int) -> int:
    q = n // 111
    if n % 111 != 0:
        q += 1

    return 111 * q


def main():
    n = int(input())
    print((answer(n)))


def __starting_point():
    main()

__starting_point()
