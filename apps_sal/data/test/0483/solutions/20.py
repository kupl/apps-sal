def main():
    input()
    l, r = [], []
    for c, x in zip(input(), list(map(int, input().split()))):
        if c == 'L':
            l.append(x)
        else:
            r.append(x)
    ilo, ihi = iter(r), iter(l)
    res = 10 ** 10
    try:
        lo, hi = next(ilo), next(ihi)
        while True:
            if lo < hi:
                if res > hi - lo:
                    res = hi - lo
                lo = next(ilo)
            else:
                hi = next(ihi)
    except StopIteration:
        print(res // 2 if res < 10 ** 10 else -1)


def __starting_point():
    main()

__starting_point()
