def resolve():
    N, A = list(map(int, input().split()))
    X = [int(i) - A for i in input().split()]
    d = {0: 1}
    for x in X:
        for _sum, count in list(d.items()):
            d[_sum + x] = d.get(_sum + x, 0) + count

    print((d[0] - 1))


if '__main__' == __name__:
    resolve()
