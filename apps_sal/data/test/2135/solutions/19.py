(h, w) = (int(x) for x in input().split())
a = [[x != '.' for x in input()] for _ in range(h)]


def build(f):
    d = [[0 for _ in range(w + 1)]]
    for r in range(h):
        d.append([0])
        for c in range(w):
            d[-1].append(d[-2][c + 1] + d[-1][c] - d[-2][c] + f(r, c))
    return d


ver = build(lambda r, c: not a[r][c] and r < h - 1 and (not a[r + 1][c]))
hor = build(lambda r, c: not a[r][c] and c < w - 1 and (not a[r][c + 1]))
for _ in range(int(input())):
    (r1, c1, r2, c2) = (int(x) for x in input().split())
    s = ver[r2 - 1][c2] - ver[r1 - 1][c2] - ver[r2 - 1][c1 - 1] + ver[r1 - 1][c1 - 1]
    s += hor[r2][c2 - 1] - hor[r1 - 1][c2 - 1] - hor[r2][c1 - 1] + hor[r1 - 1][c1 - 1]
    print(s)
