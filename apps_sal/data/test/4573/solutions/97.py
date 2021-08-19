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
    n = ni()
    X = nl()
    X_s = sorted(X)
    mid = X_s[n // 2]
    del_mid = (X_s[:n // 2] + X_s[n // 2 + 1:])[(n - 1) // 2]
    for x in X:
        if x < mid:
            print(mid)
        elif x > mid:
            print(X_s[n // 2 - 1])
        else:
            print(del_mid)


def __starting_point():
    main()


__starting_point()
