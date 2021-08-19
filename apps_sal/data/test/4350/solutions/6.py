import sys
from itertools import accumulate


def input():
    return sys.stdin.readline().strip()


def list2d(a, b, c):
    return [[c] * b for i in range(a)]


def list3d(a, b, c, d):
    return [[[d] * c for j in range(b)] for i in range(a)]


def list4d(a, b, c, d, e):
    return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]


def ceil(x, y=1):
    return int(-(-x // y))


def INT():
    return int(input())


def MAP():
    return map(int, input().split())


def LIST(N=None):
    return list(MAP()) if N is None else [INT() for i in range(N)]


def Yes():
    print('Yes')


def No():
    print('No')


def YES():
    print('YES')


def NO():
    print('NO')


INF = 10 ** 18
MOD = 10 ** 9 + 7


def build_grid(H, W, intv, _type, space=True, padding=False):
    if space:

        def _input():
            return input().split()
    else:

        def _input():
            return input()

    def _list():
        return list(map(_type, _input()))
    if padding:
        offset = 1
    else:
        offset = 0
    grid = list2d(H + offset * 2, W + offset * 2, intv)
    for i in range(offset, H + offset):
        row = _list()
        for j in range(offset, W + offset):
            grid[i][j] = row[j - offset]
    return grid


(H, W) = MAP()
grid = build_grid(H, W, '#', str, space=0, padding=1)
ans = []
imosw = list2d(H + 2, W + 2, 0)
imosh = list2d(H + 2, W + 2, 0)


def check(i, j):
    sz = min(L[i][j], R[i][j], U[i][j], D[i][j])
    if sz > 1:
        imosw[i][j - sz + 1] += 1
        imosw[i][j + sz] -= 1
        imosh[i - sz + 1][j] += 1
        imosh[i + sz][j] -= 1
        ans.append((i, j, sz - 1))


def check2():
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if grid[i][j] == '*' and (not imosw[i][j]) and (not imosh[i][j]):
                return False
    return True


L = list2d(H + 2, W + 2, 0)
R = list2d(H + 2, W + 2, 0)
U = list2d(H + 2, W + 2, 0)
D = list2d(H + 2, W + 2, 0)
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if grid[i][j] == '.':
            L[i][j] = 0
        else:
            L[i][j] = L[i][j - 1] + 1
for i in range(1, H + 1):
    for j in range(W, 0, -1):
        if grid[i][j] == '.':
            R[i][j] = 0
        else:
            R[i][j] = R[i][j + 1] + 1
for j in range(1, W + 1):
    for i in range(1, H + 1):
        if grid[i][j] == '.':
            U[i][j] = 0
        else:
            U[i][j] = U[i - 1][j] + 1
for j in range(1, W + 1):
    for i in range(H, 0, -1):
        if grid[i][j] == '.':
            D[i][j] = 0
        else:
            D[i][j] = D[i + 1][j] + 1
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if grid[i][j] == '*':
            check(i, j)
for i in range(1, H + 1):
    for j in range(W + 1):
        imosw[i][j + 1] += imosw[i][j]
for j in range(1, W + 1):
    for i in range(H + 1):
        imosh[i + 1][j] += imosh[i][j]
if check2():
    print(len(ans))
    [print(h, w, sz) for (h, w, sz) in ans]
else:
    print(-1)
