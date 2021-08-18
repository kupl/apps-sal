
import itertools
import math


def solve(n):
    for m in itertools.count(math.floor(math.sqrt(2 * n) - 1.0)):
        if 2 * n <= m * (m + 1):
            return n - (m - 1) * m // 2


def __starting_point():
    n = int(input())
    print(solve(n))


__starting_point()
