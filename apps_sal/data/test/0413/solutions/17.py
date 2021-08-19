def main():
    (n, m) = list(map(int, input().split()))
    print(rec(n, m))


def rec(n, m):
    if m <= n:
        return n - m
    elif m % 2:
        return rec(n, m + 1) + 1
    else:
        return rec(n, m // 2) + 1


def __starting_point():
    main()


__starting_point()
