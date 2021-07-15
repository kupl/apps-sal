def answer(n: int, s: str) -> str:
    if n % 2 == 1:
        return 'No'

    middle = n // 2
    if s[:middle] == s[middle:]:
        return 'Yes'

    return 'No'


def main():
    n = int(input())
    s = input()
    print((answer(n, s)))


def __starting_point():
    main()

__starting_point()
