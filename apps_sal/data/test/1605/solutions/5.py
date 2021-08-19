def main():
    s = input()
    a = [0, 0]
    b = [0, 0]
    res = [0, 0]
    for (i, c) in enumerate(s, 1):
        (ii, ij) = (i % 2, (i + 1) % 2)
        _a = a if c == 'a' else b
        res[1] += _a[ii] + 1
        res[0] += _a[ij]
        _a[ii] += 1
    print(*res)


def __starting_point():
    main()


__starting_point()
