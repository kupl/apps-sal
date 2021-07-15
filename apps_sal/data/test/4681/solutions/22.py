def answer(n: int) -> int:
    if n == 1:
        return 1

    two_previous_l = 2
    previous_l = 1
    l = 3
    for _ in range(n - 2):
        two_previous_l = previous_l
        previous_l = l
        l = previous_l + two_previous_l

    return l


def main():
    n = int(input())
    print((answer(n)))


def __starting_point():
    main()

__starting_point()
