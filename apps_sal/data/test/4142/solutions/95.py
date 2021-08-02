def answer(s: str) -> str:
    for i, c in enumerate(s):
        if i % 2 == 0:
            if c == 'L':
                return 'No'
        else:
            if c == 'R':
                return 'No'

    return 'Yes'


def main():
    s = input()
    print(answer(s))


def __starting_point():
    main()


__starting_point()
