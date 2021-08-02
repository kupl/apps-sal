from collections import deque
import math


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


h, w, n = list(map(int, input().split()))
speeds = list(map(int, input().split()))
arr = [None] * h
castles = [deque() for _ in range(n)]
castles_count = [0] * n
for i in range(h):
    arr[i] = list(input())
    for j in range(w):
        if arr[i][j] not in ('.', '#'):
            arr[i][j] = int(arr[i][j]) - 1
            castles[arr[i][j]].append((i, j))
            castles_count[arr[i][j]] += 1


def get(x):
    if (x[0] >= 0) and (x[1] >= 0) and (x[0] < h) and (x[1] < w):
        return arr[x[0]][x[1]]
    return None


has_changes = True
while has_changes:
    has_changes = False
    for p in range(n):
        cur_lvl = castles[p]
        cur_lvl_num = 0
        while (cur_lvl_num < speeds[p]) and cur_lvl:
            next_lvl = []
            for cell in cur_lvl:
                for move in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                    next_cell = add(cell, move)
                    val = get(next_cell)
                    if val == '.':
                        has_changes = True
                        next_lvl.append(next_cell)
                        arr[next_cell[0]][next_cell[1]] = p
                        castles_count[p] += 1
            cur_lvl_num += 1
            cur_lvl = next_lvl
        castles[p] = cur_lvl

print(' '.join(map(str, castles_count)))
