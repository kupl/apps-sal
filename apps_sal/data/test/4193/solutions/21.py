import numpy as np

CARD_SIZE = 3


def solve(card, called_numbers):
    checked_card = np.vectorize(lambda n: n in called_numbers)(card)

    for l in checked_card:
        if all(l):
            return True

    for l in zip(*checked_card):
        if all(l):
            return True

    if all([checked_card[n][n] for n in range(CARD_SIZE)]):
        return True
    if all([checked_card[n][CARD_SIZE - n - 1] for n in range(CARD_SIZE)]):
        return True

    return False


def resolve():
    card = [[int(row) for row in input().split()] for _ in range(CARD_SIZE)]

    N = int(input())
    called_numbers = {int(input()) for n in range(N)}

    ret = solve(card, called_numbers)

    print("Yes" if ret else "No")


def __starting_point():
    resolve()
__starting_point()
