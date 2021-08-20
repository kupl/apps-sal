def main():
    (n, k) = list(map(int, input().split()))
    k = abs(k)
    c = 0
    for y in range(2, 2 * n - k + 1):
        x = y + k
        c += counter(x, n) * counter(y, n)
    print(c)
    return


def counter(value, n):
    ins = value - 2
    return min(ins, 2 * (n - 1) - ins) + 1


def __starting_point():
    main()


__starting_point()
