# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-05-18 23:20


"""

__author__ = 'huash06'

import sys
import os
import itertools
import collections
import functools
import bisect
import datetime



DELTA = [(1, 0 ), (-1, 0), (0, -1), (0, 1)]

def existsPath(board, sr, sc, er, ec):
    visited = {(sr, sc)}
    q = [(sr, sc)]
    while q:
        r, c = q.pop(0)

        for d in DELTA:
            nr = r + d[0]
            nc = c + d[1]
            if nr == er and nc == ec:
                return True
            if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visited and board[nr][nc] == '.':
                visited.add((nr, nc))
                q.append((nr, nc))

    return False

def isNeighbor(sr, sc, er, ec):
    for d in DELTA:
        r = sr + d[0]
        c = sc + d[1]
        if r == er and c == ec:
            return True
    return False

N, M = list(map(int, input().split()))

board = []
for i in range(N):
    board.append([x for x in input()])

sr, sc = list(map(int, input().split()))
er, ec = list(map(int, input().split()))

sr -= 1
sc -= 1
er -= 1
ec -= 1


if board[er][ec] == 'X':
    if existsPath(board, sr, sc, er, ec):
        print('YES')
    else:
        print('NO')
else:
    itactNeighbor = 0
    for d in DELTA:
        r = er + d[0]
        c = ec + d[1]
        if 0 <= r < N and 0 <= c < M and board[r][c] == '.':
            itactNeighbor += 1

    if itactNeighbor > 1:
        if existsPath(board, sr, sc, er, ec):
            print('YES')
        else:
            print('NO')
    else:
        if itactNeighbor == 1 and isNeighbor(sr, sc, er, ec):
            print('YES')
        else:
            print('NO')




