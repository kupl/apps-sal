import math
from collections import defaultdict as dd
from sys import stdin, stdout
input = stdin.readline


def geti():
    return list(map(int, input().strip().split()))


def getl():
    return list(map(int, input().strip().split()))


def gets():
    return input()


def geta():
    return int(input())


def print_s(s):
    stdout.write(s + '\n')


def solve():
    for _ in range(geta()):
        (n, m) = geti()
        ok = False
        for i in range(n):
            (a, b) = geti()
            (c, d) = geti()
            if b == c:
                ok = True
        if ok and m & 1 == 0:
            print('YES')
        else:
            print('NO')


def __starting_point():
    solve()


__starting_point()
