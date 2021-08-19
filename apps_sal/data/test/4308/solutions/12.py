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
    (n, k) = nm()
    print(0 if n % k == 0 else 1)


def __starting_point():
    main()


__starting_point()
