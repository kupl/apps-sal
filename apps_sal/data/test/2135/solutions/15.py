def main():
    (h, w) = list(map(int, input().split()))
    l = [[c == '.' for c in input()] for _ in range(h)]
    ver = [[0] * (w + 1) for _ in range(h + 1)]
    for (y, aa, bb, l0, l1) in zip(list(range(h - 1)), ver, ver[1:], l, l[1:]):
        for x in range(w):
            bb[x + 1] = (l0[x] and l1[x]) + bb[x] + aa[x + 1] - aa[x]
    hor = [[0] * (w + 1) for _ in range(h + 1)]
    for (y, aa, bb, l0) in zip(list(range(h)), hor, hor[1:], l):
        for x in range(w - 1):
            bb[x + 1] = (l0[x] and l0[x + 1]) + bb[x] + aa[x + 1] - aa[x]
    res = []
    for _ in range(int(input())):
        (r1, c1, r2, c2) = list(map(int, input().split()))
        r1 -= 1
        c1 -= 1
        res.append(str(ver[r2 - 1][c2] - ver[r1][c2] - ver[r2 - 1][c1] + ver[r1][c1] + hor[r2][c2 - 1] - hor[r1][c2 - 1] - hor[r2][c1] + hor[r1][c1]))
    print('\n'.join(res))


def __starting_point():
    main()


__starting_point()
