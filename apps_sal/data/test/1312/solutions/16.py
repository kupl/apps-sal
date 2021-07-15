def main():
    n, m = list(map(int, input().split()))
    n, r = divmod(n, m)
    print(" ".join([str(n)] * (m - r) + [str(n + 1)] * r))


def __starting_point():
    main()

__starting_point()
