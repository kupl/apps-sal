

import sys

inf = float("inf")
mod = 1000000007


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return list(map(int, sys.stdin.readline().split()))


def input(): return sys.stdin.readline()


def main():
    for tc in range(int(input())):
        l1, r1, l2, r2 = get_ints()
        if l1 != l2:
            print(l1, l2)
        else:
            print(l1, r2)


def __starting_point():
    main()


__starting_point()
