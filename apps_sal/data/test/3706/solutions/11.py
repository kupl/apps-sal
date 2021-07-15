def main():
    n, m = list(map(int, input().split()))
    l, r = [list(map(int, input().split())) for _ in range(n)], []
    if n > m:
        l = [list(col) for col in zip(*l)]
        cols, rows = 'row %d', 'col %d'
    else:
        cols, rows = 'col %d', 'row %d'
    for y, row in enumerate(l, 1):
        a = min(row)
        for i, t in enumerate(row):
            row[i] = t - a
        r += [rows % y] * a
    l = [list(col) for col in zip(*l)]
    for x, col in enumerate(l, 1):
        a = min(col)
        for i, t in enumerate(col):
            col[i] = t - a
        r += [cols % x] * a
    r.append(str(len(r)))
    print(-1 if any(map(any, l)) else '\n'.join(r[::-1]))


def __starting_point():
    main()

__starting_point()
