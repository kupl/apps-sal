def answer(n: int) -> str:
    for i in range(n // 4 + 1):
        for j in range(n // 7 + 1):
            if n == i * 4 + j * 7:
                return 'Yes'

    return 'No'


def main():
    n = int(input())
    print((answer(n)))


def __starting_point():
    main()

__starting_point()
