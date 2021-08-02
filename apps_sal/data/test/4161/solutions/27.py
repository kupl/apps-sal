from collections import defaultdict
from math import gcd


def answer(k: int) -> int:
    dd = defaultdict(int)
    for a in range(1, k + 1):
        for b in range(1, k + 1):
            dd[gcd(a, b)] += 1

    gcd_sum = 0
    for c in range(1, k + 1):
        for gcd_ab in dd.keys():
            gcd_sum += gcd(gcd_ab, c) * dd[gcd_ab]

    return gcd_sum


def main():
    k = int(input())
    print(answer(k))


def __starting_point():
    main()


__starting_point()
