def answer(n: str, s: str) -> str:
    return 'Three' if len(set(s.split())) == 3 else 'Four'


def main():
    n = input()
    s = input()
    print(answer(n, s))


def __starting_point():
    main()
__starting_point()
