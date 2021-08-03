import re


def answer(a: int, b: int, s: str) -> str:
    pattern = fr'\d{{{a}}}-\d{{{b}}}'
    if re.match(pattern, s):
        return 'Yes'
    return 'No'


def main():
    a, b = list(map(int, input().split()))
    s = input()
    print((answer(a, b, s)))


def __starting_point():
    main()


__starting_point()
