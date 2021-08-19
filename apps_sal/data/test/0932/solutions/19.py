from functools import reduce


def foldM0(mat, n, m, f):
    ret = [x[:] for x in mat]
    for i in range(n):
        v = reduce(f, [mat[i][j] for j in range(m)])
        for j in range(m):
            ret[i][j] = v
    for i in range(m):
        v = reduce(f, [mat[j][i] for j in range(n)])
        for j in range(n):
            ret[j][i] = f(ret[j][i], v)
    return ret


def solve(mat, n, m):
    matpo = foldM0(mat, n, m, lambda x, y: x & y)
    if mat == foldM0(matpo, n, m, lambda x, y: x | y):
        print('YES')
        print('\n'.join((' '.join((str(x) for x in xs)) for xs in matpo)))
    else:
        print('NO')


(n, m) = map(int, input().split())
mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))
solve(mat, n, m)
