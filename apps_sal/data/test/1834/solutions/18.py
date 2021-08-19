def main():
    n = int(input())
    (a, r) = (sorted(map(int, input().split())), [0] * n)
    (r[::2], r[1::2]) = (a[:n - n // 2], a[-1:n - n // 2 - 1:-1])
    print(' '.join(map(str, r)))


def __starting_point():
    main()


__starting_point()
