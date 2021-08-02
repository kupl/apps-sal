#!/usr/bin/env python3

N = int(input())
grid = [input() for _ in range(N)]

rows = [0 for _ in range(N)]
cols = [0 for _ in range(N)]

for i in range(N):
    for j in range(N):
        if grid[i][j] == 'C':
            rows[i] += 1
            cols[j] += 1
#


def blah(n):
    return n * (n - 1) // 2


total = sum(map(blah, rows)) + sum(map(blah, cols))
print(total)
