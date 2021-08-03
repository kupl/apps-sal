from collections import defaultdict as dd
import math
import sys
input = sys.stdin.readline


def nn():
    return int(input())


def li():
    return list(input())


def mi():
    return list(map(int, input().split()))


def lm():
    return list(map(int, input().split()))


def solve():
    n, m, x, y = mi()

    print(x, y)
    for i in range(1, m + 1):
        if not i == y:
            print(x, i)
    par = 1
    for j in range(1, n + 1):
        if not j == x:
            if par == 0:
                for i in range(1, m + 1):
                    print(j, i)
            if par == 1:
                for i in reversed(list(range(1, m + 1))):
                    print(j, i)
            par = (par + 1) % 2

    return


q = 1
for _ in range(q):
    solve()
