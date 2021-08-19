n = int(input())
a = [list(map(int, input().split())) for i in range(n)]


def OnLine(A, B, C, x, y):
    return A * x + B * y + C == 0


def OffLine(A, B, C, nodes):
    res = []
    for i in nodes:
        if not OnLine(A, B, C, i[0], i[1]):
            res.append(i)
    return res


flag = False
if n < 5:
    print('YES')
    raise SystemExit
for comb in __import__('itertools').combinations([0, 1, 2], 2):
    (i, j) = (comb[0], comb[1])
    b = OffLine(a[j][1] - a[i][1], a[i][0] - a[j][0], a[j][0] * a[i][1] - a[i][0] * a[j][1], a)
    if len(b) < 3:
        print('YES')
        raise SystemExit
    if not OffLine(b[j][1] - b[i][1], b[i][0] - b[j][0], b[j][0] * b[i][1] - b[i][0] * b[j][1], b):
        print('YES')
        raise SystemExit
print('NO')
