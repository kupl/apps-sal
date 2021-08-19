def main():
    import sys
    sys.setrecursionlimit(1000000)
    (h, w, d) = list(map(int, input().split()))
    p = []
    for i in range(1, h + 1):
        l = list(map(int, input().split()))
        for (j, k) in enumerate(l, 1):
            p.append((k, (i, j)))
    p.sort(key=lambda x: x[0])
    q = int(input())
    dist = [0] * (w * h + 1)

    def Q(i, c, x, y):
        if i + d > w * h:
            return
        (_, (nx, ny)) = p[i + d - 1]
        nc = c + abs(nx - x) + abs(ny - y)
        dist[i + d] = nc
        Q(i + d, nc, nx, ny)
    for i in range(d):
        (n, (x, y)) = p[i]
        Q(n, 0, x, y)
    res = []
    for _ in range(q):
        (l, r) = list(map(int, input().split()))
        res.append(dist[r] - dist[l])
    ans = '\n'.join(map(str, res))
    print(ans)


def __starting_point():
    main()


__starting_point()
