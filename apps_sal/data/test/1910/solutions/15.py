import sys


def fact(k):
    return k ** 2 * (k - 1) ** 2 * (k - 2) ** 2 * (k - 3) ** 2 * (k - 4) ** 2


n = int(input())

print(4 ** (n - 3) * 3 * (8 + 3 * (n - 3)))

