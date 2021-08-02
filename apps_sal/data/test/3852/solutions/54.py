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


def read_values(): return list(map(int, input().split()))
def read_index(): return [int(x) - 1 for x in input().split()]
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


def main():
    N = int(input())
    A = read_list()
    M = max(A)
    m = min(A)

    T = M if abs(M) >= abs(m) else m
    i = A.index(T) + 1
    ans = []
    if T >= 0:
        for j, a in enumerate(A):
            if a < 0:
                ans.append((i, j + 1))
        for i in range(N - 1):
            ans.append((i + 1, i + 2))
    else:
        for j, a in enumerate(A):
            if a > 0:
                ans.append((i, j + 1))
        for i in range(N - 1, 0, -1):
            ans.append((i + 1, i))

    print((len(ans)))
    for a, b in ans:
        A[b - 1] += A[a - 1]
        print((a, b))


def __starting_point():
    main()


__starting_point()
