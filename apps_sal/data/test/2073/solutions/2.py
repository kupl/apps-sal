def main():
    (n, m) = (int(input()), 1000000007)
    (aa, idx) = ([0, *list(map(int, input().split()))], [0] * (n + 1))
    res = pos = 1
    for i in range(1, n + 1):
        if not idx[i]:
            (j, start) = (i, pos)
            while not idx[j]:
                idx[j] = pos
                pos += 1
                j = aa[j]
            if idx[j] >= start:
                n -= pos - idx[j]
                res = res * (pow(2, pos - idx[j], m) - 2) % m
    print(res * pow(2, n, m) % m)


def __starting_point():
    main()


__starting_point()
