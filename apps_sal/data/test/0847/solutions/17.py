import math


def main():
    (n, x) = [int(i) for i in input().split()]
    cards = [int(i) for i in input().split()]
    print(math.ceil(abs(sum(cards)) / x))


def __starting_point():
    main()


__starting_point()
