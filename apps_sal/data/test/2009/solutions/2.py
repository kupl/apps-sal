import sys
sys.setrecursionlimit(100000)


def hypot(a, b):
    return a ** 2 + b ** 2


def bfs0(r, c):
    nonlocal used
    used[r][c] = True
    comp0.append((r, c))
    if r > 0:
        if not used[r - 1][c] and matr[r - 1][c]:
            bfs0(r - 1, c)
    if r < n - 1:
        if not used[r + 1][c] and matr[r + 1][c]:
            bfs0(r + 1, c)
    if c > 0:
        if not used[r][c - 1] and matr[r][c - 1]:
            bfs0(r, c - 1)
    if c < n - 1:
        if not used[r][c + 1] and matr[r][c + 1]:
            bfs0(r, c + 1)


def bfs1(r, c):
    nonlocal used
    used[r][c] = True
    comp1.append((r, c))
    if r > 0:
        if not used[r - 1][c] and matr[r - 1][c]:
            bfs1(r - 1, c)
    if r < n - 1:
        if not used[r + 1][c] and matr[r + 1][c]:
            bfs1(r + 1, c)
    if c > 0:
        if not used[r][c - 1] and matr[r][c - 1]:
            bfs1(r, c - 1)
    if c < n - 1:
        if not used[r][c + 1] and matr[r][c + 1]:
            bfs1(r, c + 1)


n = int(input())
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
matr = [[] for i in range(n)]
for i in range(n):
    for el in input():
        if el == '0':
            matr[i].append(True)
        else:
            matr[i].append(False)
# print(matr)
used = [[False] * n for i in range(n)]
comp0 = []
bfs0(r1 - 1, c1 - 1)
if used[r2 - 1][c2 - 1]:
    print(0)
else:
    comp1 = []
    mi = 100000000000000
    bfs1(r2 - 1, c2 - 1)
    for el in comp0:
        for ell in comp1:
            mi = min(hypot(ell[0] - el[0], ell[1] - el[1]), mi)
    print(mi)
