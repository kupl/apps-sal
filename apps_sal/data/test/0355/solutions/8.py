#!/usr/bin/env python3

from sys import stdin

linecount = 8
field = []


def move_count(row, column, direction):
    if direction == 1:
        last = linecount
    else:
        last = -1

    count = 0

    for i in range(row + direction, last, direction):
        if field[i][c] != '.':
            return linecount
        else:
            count += 1

    return count



for i in range(0, linecount):
    field.append(list(stdin.readline().strip()))

a_moves = linecount
b_moves = linecount

for r in range(0, linecount):
    for c in range(0, linecount):
        if field[r][c] == 'W':
            count = move_count(r, c, -1)

            if count < a_moves:
                a_moves = count
        elif field[r][c] == 'B':
            count = move_count(r, c, 1)

            if count < b_moves:
                b_moves = count

if a_moves <= b_moves:
    print('A')
else:
    print('B')

