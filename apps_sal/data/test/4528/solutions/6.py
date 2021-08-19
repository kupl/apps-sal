import sys


def main():
    x = 24 * 60
    for tc in range(int(input())):
        (h, m) = get_ints()
        y = h * 60 + m
        print(x - y)


def get_array():
    return list(map(int, sys.stdin.readline().split()))


def get_ints():
    return list(map(int, sys.stdin.readline().split()))


def input():
    return sys.stdin.readline().strip()


def __starting_point():
    main()


__starting_point()
