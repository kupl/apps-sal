

import sys

inf = float("inf")
mod = 1000000007


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return list(map(int, sys.stdin.readline().split()))


def input(): return sys.stdin.readline()


def main():
    for tc in range(int(input())):
        n, a, b = get_ints()
        if 2 * a < b:
            print(n * a)
        else:
            print(n // 2 * b + (n % 2) * a)


def __starting_point():
    main()


__starting_point()
