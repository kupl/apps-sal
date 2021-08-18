import os
import sys
import math


def main():
    testcase()


def testcase():
    n, m = [int(x) for x in input().split()]
    table = []
    for i in range(n):
        table.append(list(input()))
    if solve(table, n, m):
        print("YES")
    else:
        print("NO")


def solve(l, n, m):
    for i in range(n):
        for j in range(m):
            try:
                z = int(l[i][j])
            except ValueError:
                if l[i][j] == '.':
                    z = 0
                else:
                    continue
            if z != neighbours(l, i, j):
                debug("i,j:", i, j)
                return False
    return True


def neighbours(l, i, j):
    n = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    s = 0
    for x, y in n:
        try:
            if j + y >= 0 and i + x >= 0:
                s += (1 if l[i + x][j + y] == '*' else 0)
        except IndexError:
            pass
    return s


def debug(*args):
    if 'DEBUG' in os.environ:
        print(*args)


def __starting_point():
    main()


__starting_point()
