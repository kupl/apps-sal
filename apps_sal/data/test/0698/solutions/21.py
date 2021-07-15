def main():
    x, k = map(int, input().split())
    l = [(0, 0)]
    for _ in range(k):
        tmp = list(map(int, input().split()))
        l.append((tmp[1], tmp[-1]))
        l.sort()
    l.append((x, x))
    mi = ma = 0
    for (a, b), (c, _) in zip(l, l[1:]):
        x = c - b
        mi += x // 2
        ma += x - 1
    print(mi, ma)


def __starting_point():
    main()
__starting_point()
