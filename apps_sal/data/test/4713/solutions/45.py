def answer(n: int, s: str) -> int:
    while 'DI' in s:
        s = s.replace('DI', '')

    return s.count('I')


def main():
    n = int(input())
    s = input()
    print(answer(n, s))


def __starting_point():
    main()


__starting_point()
