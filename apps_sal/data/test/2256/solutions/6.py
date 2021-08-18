

import sys


def main():
    for tc in range(int(input())):
        n, x, a, b = get_ints()
        a -= 1
        b -= 1
        if a > b:
            a, b = b, a
        while x > 0 and a > 0:
            x -= 1
            a -= 1
        while x > 0 and b < n - 1:
            x -= 1
            b += 1
        print(b - a)


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return list(map(int, sys.stdin.readline().split()))


def input(): return sys.stdin.readline().strip()


def __starting_point():
    main()


__starting_point()
