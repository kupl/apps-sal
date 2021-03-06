import bisect
import copy
import heapq
import sys
import itertools
import math
import queue
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7


def read_values():
    return list(map(int, input().split()))


def read_index():
    return [int(x) - 1 for x in input().split()]


def read_list():
    return list(read_values())


def read_lists(N):
    return [read_list() for n in range(N)]


def init_dp1(init, N):
    return [init for _ in range(N)]


def init_dp2(init, N, M):
    return [[init for _ in range(M)] for _ in range(N)]


class V:

    def __init__(self, f, v=None):
        self.f = f
        self.v = v

    def __str__(self):
        return str(self.v)

    def ud(self, n):
        if n is None:
            return
        if self.v is None:
            self.v = n
            return
        self.v = self.f(self.v, n)


def main():
    (N, Z, W) = read_values()
    A = read_list()
    res = V(max, abs(W - A[-1]))
    if N >= 2:
        res.ud(abs(A[-1] - A[-2]))
    print(res)


def __starting_point():
    main()


__starting_point()
