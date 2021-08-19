import sys


def IS():
    return sys.stdin.readline().rstrip()


def II():
    return int(IS())


def MII():
    return list(map(int, IS().split()))


def MIIZ():
    return list(map(lambda x: x - 1, MII()))


def main():
    (a, b, c, d) = MII()
    print(max(min(b, d) - max(a, c), 0))


def __starting_point():
    main()


__starting_point()
