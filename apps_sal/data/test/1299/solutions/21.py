def main():
    from itertools import accumulate
    (n, k) = list(map(int, input().split()))
    l = [0]
    l.extend(accumulate(list(map(int, input().split()))))
    ma = mab = 0
    for (i, x, y, z) in zip(list(range(1, n)), l, l[k:], l[k * 2:]):
        if ma < y - x:
            (t, ma) = (i, y - x)
        if mab < ma + z - y:
            (a, b, mab) = (t, i, ma + z - y)
    print(a, b + k)


def __starting_point():
    main()


__starting_point()
