def answer(n: int, s: str) -> int:
    return s.count('ABC')


def main():
    n = int(input())
    s = input()
    print(answer(n, s))


def __starting_point():
    main()


__starting_point()
