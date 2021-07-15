def answer(a: int, b: int) -> int:
    return sum(range(1, b - a + 1)) - b


def main():
    a, b = list(map(int, input().split()))
    print((answer(a, b)))


def __starting_point():
    main()

__starting_point()
