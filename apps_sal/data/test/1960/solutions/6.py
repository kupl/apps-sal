# a simple parser for python. use get_number() and get_word() to read
def main():
    def parser():
        while 1:
            data = list(input().split(' '))
            for number in data:
                if len(number) > 0:
                    yield(number)

    input_parser = parser()
    def gets(): return next(input_parser)

    def getNum():
        data = gets()
        try:
            return int(data)
        except ValueError:
            return float(data)
    # ---------program---------
    from bisect import bisect_left  # as bisect_left
    MAXA = int(9e9)
    n = getNum()
    RANGN = range(n)
    a = [getNum() for _ in RANGN]

    revlis = []
    g = [MAXA] * n
    for i in reversed(RANGN):
        x = -a[i]
        pt = bisect_left(g, x)
        revlis.append(pt + 1)
        if(x < g[pt]):
            g[pt] = x
    hlis = max(revlis)

    lis, inlis = [], []
    d = [0] * n
    for i in RANGN:
        g[i] = MAXA
    for i in RANGN:
        pt = bisect_left(g, a[i])
        lis.append(pt + 1)
        inlis.append(lis[i] + revlis[n - i - 1] > hlis)
        d[pt] += inlis[-1]
        if(a[i] < g[pt]):
            g[pt] = a[i]

    print(''.join(
        ['32'[d[lis[i] - 1] > 1] if inlis[i] else '1'
          for i in RANGN]
    ))


def __starting_point():
    main()


__starting_point()
