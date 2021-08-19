def debt(n, r):
    for i in range(n):
        (a, b, c) = [int(i) for i in input().split()]
        r[a - 1] -= c
        r[b - 1] += c
    r = [abs(i) for i in r]
    return int(sum(r) / 2)


def main():
    (n, m) = [int(i) for i in input().split()]
    r = [0 for i in range(n)]
    print(debt(m, r))


def __starting_point():
    main()


__starting_point()
