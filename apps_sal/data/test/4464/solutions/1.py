def answer(a: int, b: int, c: int) -> str:
    for i in range(1, b + 1):
        if a * i % b == c:
            return 'YES'
    return 'NO'


def main():
    (a, b, c) = map(int, input().split())
    print(answer(a, b, c))


def __starting_point():
    main()


__starting_point()
