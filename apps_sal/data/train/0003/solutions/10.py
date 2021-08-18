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
    n, k = getList()
    li = getList()

    if k >= n:
        print(sum(li))
        return

    li.sort(reverse=True)
    print(sum(li[:k + 1]))

    return


def main():
    n = getN()
    for _ in range(n):
        solve()

    return


def __starting_point():
    main()


__starting_point()
