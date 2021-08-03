def answer(s: str) -> str:
    return 'yes' if len(s) == len(set(s)) else 'no'


def main():
    s = input()
    print(answer(s))


def __starting_point():
    main()


__starting_point()
