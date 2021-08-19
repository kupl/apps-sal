import math
import sys
from collections import defaultdict
input = sys.stdin.readline


def main():
    (n, k) = list(map(int, input().split()))
    grid = [[] for _ in range(n)]
    for i in range(n):
        grid[i] = list(input().strip())
    row_min = [math.inf] * n
    row_max = [math.inf] * n
    col_min = [math.inf] * n
    col_max = [math.inf] * n
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'B':
                row_min[i] = min(row_min[i], j)
                row_max[i] = j
            if grid[j][i] == 'B':
                col_min[i] = min(col_min[i], j)
                col_max[i] = j
    res = 0
    for r in range(n):
        if row_min[r] == math.inf:
            res += 1
    for c in range(n):
        if col_min[c] == math.inf:
            res += 1
    rows_plus = [[0 for _ in range(n)] for _ in range(n)]
    for c in range(n - k + 1):
        added = 0
        for r in range(k):
            if row_min[r] >= c and row_max[r] <= c + k - 1:
                added += 1
        rows_plus[0][c] = added
        r = 1
        while r + k - 1 < n:
            if row_min[r - 1] >= c and row_max[r - 1] <= c + k - 1:
                added -= 1
            if row_min[r + k - 1] >= c and row_max[r + k - 1] <= c + k - 1:
                added += 1
            rows_plus[r][c] = added
            r += 1
    cols_plus = [[0 for _ in range(n)] for _ in range(n)]
    for r in range(n - k + 1):
        added = 0
        for c in range(k):
            if col_min[c] >= r and col_max[c] <= r + k - 1:
                added += 1
        cols_plus[r][0] = added
        c = 1
        while c + k - 1 < n:
            if col_min[c - 1] >= r and col_max[c - 1] <= r + k - 1:
                added -= 1
            if col_min[c + k - 1] >= r and col_max[c + k - 1] <= r + k - 1:
                added += 1
            cols_plus[r][c] = added
            c += 1
    max_added = 0
    for r in range(n):
        for c in range(n):
            max_added = max(max_added, rows_plus[r][c] + cols_plus[r][c])
    print(res + max_added)


def __starting_point():
    main()


__starting_point()
