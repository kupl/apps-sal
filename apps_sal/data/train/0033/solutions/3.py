import sys
import random
import math
import copy
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
input = sys.stdin.readline
def getS(): return input().strip()
def getN(): return int(input())
def getList(): return list(map(int, input().split()))
def getZList(): return [int(x) - 1 for x in input().split()]


INF = float("inf")

MOD = 10 ** 9 + 7
def divide(x): return pow(x, MOD - 2, MOD)


def judge(at, ax, ay, bt, bx, by):
    if abs(at - bt) >= abs(ax - bx) + abs(ay - by):
        return True
    else:
        return False


def solve():
    n = getN()
    if n == 2:
        print(2)
        print(1, 2)
        return

    print(2)
    print(n - 2, n)
    print(n - 1, n - 1)
    for i in range(n - 3):
        print(n - 1 - i, n - 3 - i)
    return


def main():
    n = getN()
    for _ in range(n):
        solve()

    return


def __starting_point():
    main()


__starting_point()
