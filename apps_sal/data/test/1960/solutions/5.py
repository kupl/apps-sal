def main():

    def parser():
        while 1:
            data = list(input().split(' '))
            for number in data:
                if len(number) > 0:
                    yield number
    input_parser = parser()

    def gets():
        return next(input_parser)

    def getNum():
        data = gets()
        try:
            return int(data)
        except ValueError:
            return float(data)
    from bisect import bisect_left as binsleft
    MAXA = int(9000000000.0)
    n = getNum()
    RANGN = range(n)
    a = [getNum() for _ in RANGN]
    revlis = []
    g = [MAXA] * n
    for i in reversed(RANGN):
        x = -a[i]
        pt = binsleft(g, x)
        revlis.append(pt + 1)
        if x < g[pt]:
            g[pt] = x
    hlis = max(revlis)
    (lis, inlis) = ([], [])
    d = [0] * n
    for i in RANGN:
        g[i] = MAXA
    for i in RANGN:
        pt = binsleft(g, a[i])
        lis.append(pt + 1)
        inlis.append(lis[i] + revlis[n - i - 1] > hlis)
        d[pt] += inlis[-1]
        if a[i] < g[pt]:
            g[pt] = a[i]
    print(''.join(['32'[d[lis[i] - 1] > 1] if inlis[i] else '1' for i in RANGN]))


def __starting_point():
    main()


__starting_point()
