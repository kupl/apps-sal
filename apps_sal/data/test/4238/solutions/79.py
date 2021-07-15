def answer(n: str) -> str:
    return 'Yes' if sum(map(int, n.split())) % 9 == 0 else 'No'


def main():
    n = input()
    print((answer(n)))


def __starting_point():
    main()

__starting_point()
