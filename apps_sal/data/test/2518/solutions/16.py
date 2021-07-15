def main():
    from math import ceil
    n, a, b, *k = list(map(int, open(0).read().split()))
    k.sort()

    l = k[-1] // a
    r = k[-1] // b + 1
    m = (l + r) // 2
    while l + 1 < r:
        c = sum(ceil((i - m * b) / (a - b)) if i - m * b > 0 else 0 for i in k)
        if c <= m:
            r = m
        else:
            l = m

        m = (l + r) // 2

    print(r)


def __starting_point():
    main()

__starting_point()
