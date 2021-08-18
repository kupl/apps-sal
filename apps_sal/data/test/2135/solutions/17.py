import itertools
import functools
import math


def II(r1, c1, r2, c2, table):
    if r1 > r2:
        return 0
    if c1 > c2:
        return 0
    res = table[r2][c2]
    if r1:
        res -= table[r1 - 1][c2]
    if c1:
        res -= table[r2][c1 - 1]
    if r1 and c1:
        res += table[r1 - 1][c1 - 1]
    return res


def solve():
    h, w = list(map(int, input().split()))
    grid = [input() for _ in range(h)]

    row = [[0] * w for _ in range(h)]
    col = [[0] * w for _ in range(h)]

    for i in range(h):
        col_prev = 0
        row_prev = 0
        for j in range(w):
            row[i][j] = row_prev
            col[i][j] = col_prev
            if i:
                row[i][j] += row[i - 1][j]
                col[i][j] += col[i - 1][j]

            if grid[i][j] == '
            continue

            if i + 1 < h and grid[i + 1][j] != '
            row[i][j] += 1
            row_prev += 1
            if j + 1 < w and grid[i][j + 1] != '
            col[i][j] += 1
            col_prev += 1

    q = int(input())
    for _ in range(q):
        r1, c1, r2, c2 = list(map(int, input().split()))
        r1 -= 1
        c1 -= 1
        r2 -= 1
        c2 -= 1
        print(II(r1, c1, r2 - 1, c2, row) + II(r1, c1, r2, c2 - 1, col))


def __starting_point():
    solve()


__starting_point()
