3

import math
import sys


DEBUG = False


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def is_prime(a):
    x = 2
    while x * x <= a:
        if a % x == 0:
            return False
        x += 1
    return True


def main():
    N = int(inp())

    p = N
    while not is_prime(p):
        p += 1

    diff = p - N
    assert diff <= N // 2

    print(p)
    for i in range(N):
        print(i + 1, (i + 1) % N + 1)

    i = 1
    j = 1 + N // 2
    while diff > 0:
        print(i, j)
        i += 1
        j += 1
        diff -= 1


def __starting_point():
    main()

__starting_point()
