from sys import stdin, stdout
from math import *


def nStep(n):
    if (n == 0):
        return 0
    if (n == 2):
        return 1
    for i in range(2, floor(sqrt(n) + 2), 1):
        if (n % i == 0):
            if (i == 2):
                return floor(n / 2)
            else:
                return 1 + nStep(n - i)
    return 1


def main():
    n = int(stdin.readline())
    stdout.write(str(nStep(n)))
    return 0


def __starting_point():
    main()


__starting_point()
