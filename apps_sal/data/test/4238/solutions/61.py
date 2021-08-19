def answer(n: str) -> str:
    result = 0
    for i in n:
        result += int(i)
    return 'Yes' if result % 9 == 0 else 'No'


def main():
    n = input()
    print(answer(n))


def __starting_point():
    main()


__starting_point()
