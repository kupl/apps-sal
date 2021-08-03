import itertools
import math

answers = [2, 7, 2, 3, 3, 4, 2, 5, 1, 2]


def main():
    a, b = list(map(int, input()))
    print(answers[a] * answers[b])


def __starting_point():
    main()


__starting_point()
