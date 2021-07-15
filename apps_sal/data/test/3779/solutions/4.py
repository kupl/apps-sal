from math import gcd
from functools import reduce


def main():
    n, k = map(int, input().split())
    g = reduce(gcd, map(int, input().split()), k)
    print(k // g, ' '.join(map(str, range(0, k, g))), sep='\n')


def __starting_point():
    main()

__starting_point()
