def read_nums():
    return [int(x) for x in input().split()]


def main():
    (n, k) = read_nums()
    for _ in range(k):
        if n % 10 == 0:
            n = n // 10
        else:
            n = n - 1
    print(n)


def __starting_point():
    main()


__starting_point()
