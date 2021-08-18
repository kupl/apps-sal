
import math
from itertools import combinations_with_replacement as comb
from functools import reduce


def main():
    K = int(input())

    ans = 0
    for abc in comb(range(1, K + 1), 3):
        gcd = reduce(math.gcd, abc)
        s = len(set(abc))
        if s == 1:
            k = 1
        elif s == 2:
            k = 3
        else:
            k = 6
        ans += gcd * k

    print(ans)


def __starting_point():
    main()


__starting_point()
