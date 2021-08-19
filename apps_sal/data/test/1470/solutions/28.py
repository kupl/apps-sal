import os
import sys


def main():
    x = int(input())
    if x % 11 == 0:
        print(2 * (x // 11))
        return
    tmp = x // 11
    ans = tmp * 2
    new = x - tmp * 11
    if 0 < new <= 6:
        print(ans + 1)
    else:
        print(ans + 2)


def __starting_point():
    main()


__starting_point()
