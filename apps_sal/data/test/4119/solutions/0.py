def main():
    (n, m) = list(map(int, input().split()))
    x = sorted(list(map(int, input().split())))
    diff = list()
    for (i, j) in zip(x, x[1:]):
        diff.append(abs(i - j))
    diff = sorted(diff, reverse=True)
    print(sum(diff) - sum(diff[:n - 1]))


def __starting_point():
    main()


__starting_point()
