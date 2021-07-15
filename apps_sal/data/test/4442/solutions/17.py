def answer(a: int, b: int) -> str:
    return min(str(a) * b, str(b) * a)


def main():
    a, b = map(int, input().split())
    print(answer(a, b))


def __starting_point():
    main()
__starting_point()
