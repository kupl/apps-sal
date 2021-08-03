def main():
    n, m, *abc = list(map(int, open(0).read().split()))
    d = [[float("Inf")] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        d[i][i] = 0

    for a, b, c in zip(*[iter(abc)] * 3):
        d[a][b] = c
        d[b][a] = c

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    ans = 0
    for a, b, c in zip(*[iter(abc)] * 3):
        if d[a][b] < c:
            ans += 1

    print(ans)


def __starting_point():
    main()


__starting_point()
