import bisect
import collections
import copy
import itertools
import math
import string
import sys


def I():
    return int(sys.stdin.readline().rstrip())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


def main():
    (w, h, n) = LI()
    board = [[1] * h for _ in range(w)]
    for _ in range(n):
        (x, y, a) = LI()
        if a == 1:
            for i in range(x):
                board[i] = [0 for _ in range(h)]
        elif a == 2:
            for i in range(x, w):
                board[i] = [0 for _ in range(h)]
        elif a == 3:
            for i in range(w):
                for j in range(y):
                    board[i][j] = 0
        elif a == 4:
            for i in range(w):
                for j in range(y, h):
                    board[i][j] = 0
    ans = 0
    for line in board:
        ans += sum(line)
    print(ans)


main()
