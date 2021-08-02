def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a = sorted(a)
    res = []
    for i in range(0, n, 2):
        res.append(a[i])
    for i in reversed(list(range(1, n, 2))):
        res.append(a[i])
    print(' '.join((str(x) for x in res)))


def __starting_point():
    main()


__starting_point()
