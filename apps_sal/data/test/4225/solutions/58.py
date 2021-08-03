def answer(a: int, b: int, c: int, k: int) -> int:
    if k <= a:
        return k
    if k <= a + b:
        return a
    return a - (k - (a + b))


def main():
    a, b, c, k = map(int, input().split())
    print(answer(a, b, c, k))


def __starting_point():
    main()


__starting_point()
