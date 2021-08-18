def abc044_c():
    _, A = map(int, input().split())
    X = list(map(lambda x: int(x) - A, input().split()))
    d = {0: 1}
    for x in X:
        for k, v in list(d.items()):
            d[k + x] = d.get(k + x, 0) + v
    ans = d[0] - 1
    print(ans)


def __starting_point():
    abc044_c()


__starting_point()
