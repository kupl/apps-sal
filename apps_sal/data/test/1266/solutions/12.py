def main():
    n = int(input())
    inf = 10 ** 10
    (x0, y0) = list(map(int, input().split()))
    (h, v, d1, d2) = ([(-inf, 'K'), (0, 'K'), (inf, 'K')] for _ in range(4))
    for _ in range(n):
        (f, x, y) = input().split()
        x = int(x) - x0
        y = int(y) - y0
        if not x:
            h.append((y, f))
        elif not y:
            v.append((x, f))
        elif x == y:
            d1.append((x, f))
        elif x == -y:
            d1.append((x, f))
    res = False
    for l in (h, v, d1, d2):
        l.sort()
    i = h.index((0, 'K'))
    if h[i - 1][1] in 'RQ':
        res = True
    if h[i + 1][1] in 'RQ':
        res = True
    i = v.index((0, 'K'))
    if v[i - 1][1] in 'RQ':
        res = True
    if v[i + 1][1] in 'RQ':
        res = True
    i = d1.index((0, 'K'))
    if d1[i - 1][1] in 'BQ':
        res = True
    if d1[i + 1][1] in 'BQ':
        res = True
    i = d2.index((0, 'K'))
    if d2[i - 1][1] in 'BQ':
        res = True
    if d2[i + 1][1] in 'BQ':
        res = True
    print(('NO', 'YES')[res])


def __starting_point():
    main()


__starting_point()
