from math import fsum


def main():
    (l, x) = ([0, 0], 0)
    for c in input():
        if c in ('I', 'E', 'A', 'O', 'U', 'Y'):
            x += 1
        l.append(x)
    n = l[-1]
    res = [float(n)]
    for m in range(2, len(l) - 1):
        n += l[-m] - l[m]
        res.append(n / m)
    print('{:.7f}'.format(fsum(res)))


def __starting_point():
    main()


__starting_point()
