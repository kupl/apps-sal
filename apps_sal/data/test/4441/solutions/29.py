import sys
stdin = sys.stdin


def ns():
    return stdin.readline().rstrip()


def ni():
    return int(stdin.readline().rstrip())


def nm():
    return list(map(int, stdin.readline().split()))


def nl():
    return list(map(int, stdin.readline().split()))


def main():
    print('Hello World' if ni() == 1 else ni() + ni())


def __starting_point():
    main()


__starting_point()
