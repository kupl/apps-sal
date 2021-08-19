from sys import stdin, setrecursionlimit
import bisect
import collections
import copy
import heapq
import itertools
import math
import string
setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 1000000007


def input():
    return stdin.readline().strip()


def main():
    n = int(input())
    ok = n + 1
    ng = 0
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if n + 1 >= (n + 1 - mid) * (n + 1 - mid + 1) // 2:
            ok = mid
        else:
            ng = mid
    print(ok)
    return


def __starting_point():
    main()


__starting_point()
