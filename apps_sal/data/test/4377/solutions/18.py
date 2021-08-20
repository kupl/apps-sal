import sys


def get_array():
    return list(map(int, sys.stdin.readline().split()))


def get_ints():
    return list(map(int, sys.stdin.readline().split()))


def input():
    return sys.stdin.readline().strip()


def main():
    p = get_array()
    p.sort()
    (a, b, c, d) = (p[0], p[1], p[2], p[3])
    z = d - a
    y = d - b
    x = d - c
    print(x, y, z)


def __starting_point():
    main()


__starting_point()
