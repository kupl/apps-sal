import math
from sys import stdin
from math import ceil
import sys


def __starting_point():
    n = int(input())
    table = list()
    newT = list()
    for i in range(n):
        table.append(input())
    for i in range(2 * n):
        newT.append([1] * (2 * n))

    for i in range(n):
        for j in range(n):
            if table[i][j] != 'o':
                continue
            for a in range(n):
                for b in range(n):
                    if table[a][b] == '.':
                        newT[n - i + a][n - j + b] = 0
    for i in range(n):
        for j in range(n):
            if table[i][j] != 'x':
                continue
            piece = 0
            for a in range(n):
                for b in range(n):
                    if table[a][b] == 'o' and newT[n + i - a][n + j - b] == 1:
                        piece = 1
                        break
                if piece == 1:
                    break
            if piece == 0:
                print("NO")
                return
    print("YES")
    for i in range(1, 2 * n):
        for j in range(1, 2 * n):
            if i == n and j == n:
                print('o', end='')
            elif newT[i][j] == 1:
                print('x', end='')
            else:
                print('.', end='')
        print('')


__starting_point()
