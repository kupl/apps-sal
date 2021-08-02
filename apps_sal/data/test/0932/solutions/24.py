def main():
    n, m = map(int, input().split())
    l = tuple(tuple(map(int, input().split())) for _ in range(n))
    res = [[1] * m for _ in range(n)]
    for y, row in enumerate(l):
        for x, f in enumerate(row):
            if not f:
                res[y] = [0] * m
                for rr in res:
                    rr[x] = 0
    for y, row in enumerate(l):
        for x, f in enumerate(row):
            if f:
                if not (any(res[y]) or any(rr[x] for rr in res)):
                    print('NO')
                    return
    print('YES')
    for rr in res:
        print(*rr)


def __starting_point():
    main()


__starting_point()
