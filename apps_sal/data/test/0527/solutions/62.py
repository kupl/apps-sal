import sys
import re
import math
import collections
import bisect
import itertools
import fractions
import functools
import copy
import heapq
import decimal
import statistics
import queue
sys.setrecursionlimit(10 ** 9)
INF = 10 ** 16
MOD = 10 ** 9 + 7


def ni():
    return int(sys.stdin.readline())


def ns():
    return list(map(int, sys.stdin.readline().split()))


def na():
    return list(map(int, sys.stdin.readline().split()))


def nb():
    return list([int(x) - 1 for x in sys.stdin.readline().split()])


def main():
    s = list(input())
    t = collections.deque(list(input()))
    jump = [[0] * 26 for _ in range(len(s) + 1)]
    for i in range(len(s) - 1, -1, -1):
        jump[i] = jump[i + 1].copy()
        jump[i][ord(s[i]) - 97] = i + 1
    ans = 0
    point = 0
    while len(t) > 0:
        tmp = t.popleft()
        character = ord(tmp) - 97
        if jump[point][character] == 0 and point == 0:
            print(-1)
            return
        point = jump[point][character]
        if point == 0:
            t.appendleft(tmp)
            ans += 1
    print(ans * len(s) + point)


def __starting_point():
    main()


__starting_point()
