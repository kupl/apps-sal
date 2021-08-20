import sys
import io
import math
import collections
import decimal
import itertools
from queue import PriorityQueue
import bisect


def input():
    return sys.stdin.readline()[:-1]


sys.setrecursionlimit(1000000)


def solve(N, a):
    x = min(a)
    while True:
        min_k = 10 ** 9
        for i in range(N):
            a[i] = a[i] % x
            if a[i] > 0:
                min_k = min(min_k, a[i])
        if min_k == 10 ** 9:
            return x
        x = min_k


def main():
    N = int(input())
    a = list(map(int, input().split()))
    a1 = solve(N, a)
    print(a1)


def __starting_point():
    main()


__starting_point()
