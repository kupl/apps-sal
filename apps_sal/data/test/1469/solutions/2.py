def main():
    L = int(input())
    r = 0
    while 2 ** (r + 1) <= L:
        r += 1
    assert r < 20
    N = r + 1
    edges = list()
    for i in range(1, N):
        edges.append((i, i + 1, 0))
        edges.append((i, i + 1, 2 ** (i - 1)))
    for t in range(N - 1, 0, -1):
        if L - 2 ** (t - 1) >= 2 ** r:
            edges.append((t, N, L - 2 ** (t - 1)))
            L -= 2 ** (t - 1)
    print('{} {}'.format(N, len(edges)))
    for e in edges:
        print(' '.join(map(str, e)))


def __starting_point():
    main()


__starting_point()
