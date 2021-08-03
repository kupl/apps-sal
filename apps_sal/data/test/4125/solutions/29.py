import math
from functools import reduce


def gcd(*numbers):
    return reduce(math.gcd, numbers)


def main():
    n, X = list(map(int, input().split()))
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    x_dist = [x[i + 1] - x[i] for i in range(len(x) - 1)]
    print((gcd(*x_dist)))


def __starting_point():
    main()


__starting_point()
