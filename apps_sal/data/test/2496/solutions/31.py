from math import gcd
from functools import reduce


def facs(n):
    yield 2
    for x in range(3, n, 2):
        yield x


def main():
    input()
    array = [int(x) for x in input().split()]
    MAX_A = 10 ** 6 + 1
    histogram = [0] * MAX_A
    for x in array:
        histogram[int(x)] += 1
    for divider in facs(MAX_A):
        count = sum(histogram[divider::divider])
        if count > 1:
            break
    else:
        return 'pairwise coprime'
    gcd_total = reduce(gcd, array)
    if gcd_total == 1:
        return 'setwise coprime'
    else:
        return 'not coprime'


def __starting_point():
    print(main())


__starting_point()
