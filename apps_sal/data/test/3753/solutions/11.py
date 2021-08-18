from collections import *
import sys


def main():
    r, c = map(int, sys.stdin.readline().strip().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(r)]
    n = sum(u.count('
    if n == 0:
        if r == 1:
            print(1)
        elif c == 1:
            print(1)
        else:
            print(2)
        return
    if r == c == 2:
        print(2 - n)
        return
    grid[0][0]='0'
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '
                continue
            f=False
            if i != 0:
                f=f or grid[i - 1][j] == '0'
            if j != 0:
                f=f or grid[i][j - 1] == '0'
            if f:
                grid[i][j]='0'

    grid[-1][-1]='1'
    for i in range(r - 1, -1, -1):
        for j in range(c - 1, -1, -1):
            if grid[i][j] != '0':
                continue
            if i != r - 1 and grid[i + 1][j] == '1':
                grid[i][j]='1'
            elif j != c - 1 and grid[i][j + 1] == '1':
                grid[i][j]='1'

    if grid[0][0] != '1':
        print(0)
        return
    dictionary=Counter()
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '1':
                dictionary[i + j] += 1
    for key in dictionary:
        if 0 < key < r + c - 2 and dictionary[key] == 1:
            print(1)
            return
    print(2)


main()
