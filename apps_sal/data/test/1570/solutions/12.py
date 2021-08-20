import sys


def main():
    (k, n, w) = map(int, sys.stdin.readline().split())
    s = k * (1 + w) * w // 2
    print(max(s - n, 0))


def __starting_point():
    main()


__starting_point()
