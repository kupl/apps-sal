def main():
    BK = '#'
    WH = '.'
    (A, B) = map(int, input().split())
    g = []
    for _ in range(50):
        g.append([BK] * 100)
    for _ in range(50):
        g.append([WH] * 100)
    (r, c) = (1, 1)
    for _ in range(A - 1):
        g[r][c] = WH
        c += 2
        if c > 99:
            c = 1
            r += 2
    (r, c) = (51, 1)
    for _ in range(B - 1):
        g[r][c] = BK
        c += 2
        if c > 99:
            c = 1
            r += 2
    print(100, 100)
    for row in g:
        print(*row, sep='')


def __starting_point():
    main()


__starting_point()
