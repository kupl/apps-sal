t = int(input())
for k in range(t):
    r8 = range(8)
    a = [input() for i in r8]
    ij = [(i, j) for i in r8 for j in r8]
    (x, y) = ((i, j) for (i, j) in ij if a[i][j] == 'K')

    def s(p):
        d = [(p[0] - 2, p[1] - 2), (p[0] + 2, p[1] - 2), (p[0] - 2, p[1] + 2), (p[0] + 2, p[1] + 2)]
        return set(((i, j) for (i, j) in ij if (i, j) in d))
    print('YES' if len(s(x) & s(y)) > 0 else 'NO')
    if k != t - 1:
        input()
