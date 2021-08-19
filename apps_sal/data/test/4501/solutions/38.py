def main():
    (N, A) = map(int, input().split())
    X = list(map(int, input().split()))
    X = [x - A for x in X]
    ret = {0: 1}
    for xi in X:
        for (y, cnt) in list(ret.items()):
            ret[xi + y] = ret.get(xi + y, 0) + cnt
    print(ret[0] - 1)


def __starting_point():
    main()


__starting_point()
