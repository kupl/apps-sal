from math import sin, pi


def solve():
    n = int(input())
    return sin((n - 1) * pi / (2 * n)) / sin(pi / (2 * n))


def main():
    t = int(input())
    print('\n'.join(map(str, [solve() for _ in range(t)])))


def __starting_point():
    main()


__starting_point()
