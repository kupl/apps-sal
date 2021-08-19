c = 1


def main():
    (n, k) = map(int, input().split())
    l = list(range(1, n * k + 1))
    aa = list(map(int, input().split()))
    for a in aa:
        l[a - 1] = 0
    (res, it) = ([], iter(filter(None, l)))
    n -= 1
    for a in aa:
        res.append(a)
        for _ in range(n):
            res.append(next(it))
        print(' '.join(map(str, res)))
        res.clear()


def __starting_point():
    main()


__starting_point()
