#!/usr/local/bin/python3

import sys

table = [line.strip() for line in sys.stdin]


def check_position(table, row, column):

    if table[row][column] != '.':
        return False

    left_sum = 0
    tmp = column - 1
    while (tmp >= 0) and table[row][tmp] == 'X':
        left_sum += 1
        tmp -= 1

    right_sum = 0
    tmp = column + 1
    while (tmp < 10) and table[row][tmp] == 'X':
        right_sum += 1
        tmp += 1

    if left_sum + right_sum >= 4:
        return True

    # -----

    up_sum = 0
    tmp = row - 1
    while (tmp >= 0) and table[tmp][column] == 'X':
        up_sum += 1
        tmp -= 1

    down_sum = 0
    tmp = row + 1
    while (tmp < 10) and table[tmp][column] == 'X':
        down_sum += 1
        tmp += 1

    if up_sum + down_sum >= 4:
        return True

    # -----

    maindup_sum = 0
    tmp_row = row - 1
    tmp_col = column - 1
    while (tmp_row >= 0) and (tmp_col >= 0) and table[tmp_row][tmp_col] == 'X':
        tmp_row -= 1
        tmp_col -= 1
        maindup_sum += 1

    maindup_down = 0
    tmp_row = row + 1
    tmp_col = column + 1
    while (tmp_row < 10) and (tmp_col < 10) and table[tmp_row][tmp_col] == 'X':
        tmp_row += 1
        tmp_col += 1
        maindup_down += 1

    if maindup_sum + maindup_down >= 4:
        return True

    # -----

    dup_sum = 0
    tmp_row = row - 1
    tmp_col = column + 1
    while (tmp_row >= 0) and (tmp_col < 10) and table[tmp_row][tmp_col] == 'X':
        tmp_row -= 1
        tmp_col += 1
        dup_sum += 1

    dup_down = 0
    tmp_row = row + 1
    tmp_col = column - 1
    while (tmp_row < 10) and (tmp_col >= 0) and table[tmp_row][tmp_col] == 'X':
        tmp_row += 1
        tmp_col -= 1
        dup_down += 1

    if dup_sum + dup_down >= 4:
        return True

    return False


for row in range(10):
    for column in range(10):
        if check_position(table, row, column):
            print("YES")
            return

print("NO")
