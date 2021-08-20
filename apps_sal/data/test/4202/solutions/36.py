import os
import sys


def main():
    (L, R) = list(map(int, input().split()))
    cool = R // 2019 - L // 2019
    if cool == 0:
        ans = 2020
        for l in range(L, R + 1):
            for r in range(l + 1, R + 1):
                if ans > l * r % 2019:
                    ans = l * r % 2019
        print(ans)
    else:
        print(0)


def __starting_point():
    main()


__starting_point()
