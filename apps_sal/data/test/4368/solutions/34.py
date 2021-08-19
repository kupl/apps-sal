def answer(n: int, k: int) -> int:
    digits = 0
    while 0 < n:
        n //= k
        digits += 1
    return digits


def main():
    (n, k) = map(int, input().split())
    print(answer(n, k))


def __starting_point():
    main()


__starting_point()
