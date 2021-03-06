import re


def answer(s: str) -> str:
    pattern = 'A[a-z]+C[a-z]+'
    return 'AC' if re.fullmatch(pattern, s) else 'WA'


def main():
    s = input()
    print(answer(s))


def __starting_point():
    main()


__starting_point()
