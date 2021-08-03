import bisect


def __starting_point():

    n, m = [int(x) for x in input().strip().split()]
    a = sorted([int(x) for x in input().strip().split()])
    b = [int(x) for x in input().strip().split()]

    res = []
    for bi in b:
        pos = bisect.bisect_left(a, bi)
        if pos < n and a[pos] == bi:
            res.append(bisect.bisect_right(a, bi))
        else:
            res.append(pos)

    print(" ".join([str(x) for x in res]))


__starting_point()
