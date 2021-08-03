def answer(x: int, y: int) -> str:
    if x * 2 <= y <= x * 4 and y % 2 == 0:
        return 'Yes'
    return 'No'


def main():
    x, y = map(int, input().split())
    print(answer(x, y))


def __starting_point():
    main()


__starting_point()
