def main():
    n, m = map(int, input().split())
    d = {}
    for _ in range(m):
        a, b = input().split()
        d[a] = d[b] = b if len(a) > len(b) else a
    print(' '.join([d[_] for _ in input().split()]))


def __starting_point():
    main()


__starting_point()
