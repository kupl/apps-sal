"""
1
0

0

1

0
"""
import sys
n = int(input())


def read_board(n, numb):
    board = []
    for i in range(n):
        line = input()
        board.append([int(c) for c in line])
    if numb != 3:
        input()
    return board


boards = [read_board(n, i) for i in range(4)]


def _calc_line(l, start=1):
    cur = start
    errors = 0
    for cell in l:
        errors += cell != cur
        cur = not cur
    return errors


def _calc_board(b, start=1):
    errors = 0
    cur = start
    for line in b:
        errors += _calc_line(line, cur)
        cur = not cur
    return errors


checks = [(0, 0, 1, 1), (0, 1, 0, 1), (1, 0, 0, 1), (0, 1, 1, 0), (1, 0, 1, 0), (1, 1, 0, 0)]


def check_all(boards):
    for check in checks:
        errs = 0
        for (board, start) in zip(boards, check):
            errs += _calc_board(board, start)
        yield errs


print(min(check_all(boards)))
