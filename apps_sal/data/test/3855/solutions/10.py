from math import log2


def __starting_point():
    n = int(input())
    l = int(log2(n)) + 1
    if 2 ** l < n:
        l += 1
    print(l)

__starting_point()
