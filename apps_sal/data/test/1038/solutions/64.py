import sys
from collections import Counter as cc


def input():
    return sys.stdin.readline().rstrip()


def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


def main():
    (a, b) = mi()

    def sxor(x):
        ret = (x + 1) // 2 % 2
        if x % 2 == 0:
            ret ^= x
        return ret
    ans = sxor(b) ^ sxor(a - 1)
    print(ans)


def __starting_point():
    main()


__starting_point()
