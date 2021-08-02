import re


def answer(s: str) -> int:
    pattern = r'[ACTG]+'
    result = re.findall(pattern, s)
    if not result:
        return 0

    return len(max(result, key=len))


def main():
    s = input()
    print((answer(s)))


def __starting_point():
    main()


__starting_point()
