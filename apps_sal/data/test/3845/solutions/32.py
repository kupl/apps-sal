import sys
import numpy as np
stdin = sys.stdin


def ri():
    return int(rs())


def rl():
    return list(map(int, stdin.readline().split()))


def rs():
    return stdin.readline().rstrip()


(A, B) = rl()
grid = [['.'] * 100 for _ in range(50)] + [['#'] * 100 for _ in range(50)]
for i in range(B - 1):
    (row, column) = divmod(i, 50)
    row *= 2
    column *= 2
    grid[row][column] = '#'
for i in range(A - 1):
    (row, column) = divmod(i, 50)
    row *= 2
    column *= 2
    grid[99 - row][column] = '.'
print(100, 100)
for x in grid:
    print(*x, sep='')
