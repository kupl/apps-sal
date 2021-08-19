def abc044_c():
    """ 過去提出を参考に """
    (_, A) = map(int, input().split())
    X = list(map(lambda x: int(x) - A, input().split()))
    d = {0: 1}
    for x in X:
        prev = list(d.items())
        for (val, cnt) in prev:
            d[val + x] = d.get(val + x, 0) + cnt
    ans = d[0] - 1
    print(ans)


def __starting_point():
    abc044_c()


__starting_point()
