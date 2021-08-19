from sys import stdin


def rs():
    return stdin.readline().strip()


def ri():
    return int(rs())


def ril():
    return list(map(int, rs().split()))


def main():
    N = ri()
    a = ril()
    print(max(a) - min(a))


def __starting_point():
    main()


__starting_point()
