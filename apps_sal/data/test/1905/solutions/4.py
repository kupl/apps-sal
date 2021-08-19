(m, n, q) = map(int, input().split())
inps = [map(lambda x: int(x) - 1, input().split()) for _ in range(q)]
matrix = [[-1] * n for _ in range(m)]
for x in reversed(inps):
    (t, c, *cc) = x
    if t == 0:
        matrix[c] = [matrix[c][-1]] + matrix[c][:-1]
    elif t == 1:
        new = [matrix[i][c] for i in range(m)]
        for (i, x) in enumerate([new[-1]] + new[:-1]):
            matrix[i][c] = x
    elif t == 2:
        matrix[c][cc[0]] = cc[1]
for x in matrix:
    print(' '.join(map(lambda v: str(v + 1), x)))
