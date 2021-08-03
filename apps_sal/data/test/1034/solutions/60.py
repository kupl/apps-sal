from collections import Counter, deque
import bisect
import itertools
import sys
import math
from math import gcd, pi, sqrt
INF = float("inf")
MOD = 10**9 + 7

sys.setrecursionlimit(10**6)
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]


def main():
    import heapq

    X, Y, Z, K = i_map()
    A = i_list()
    B = i_list()
    C = i_list()

    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    Q = []
    heapq.heappush(Q, [-(A[0] + B[0] + C[0]), 0, 0, 0])
    added_idx = set((0, 0, 0))

    for i in range(K):
        nega_ans, x, y, z = heapq.heappop(Q)
        print(-nega_ans)

        if x + 1 < X and (x + 1, y, z) not in added_idx:
            heapq.heappush(Q, [-(A[x + 1] + B[y] + C[z]), x + 1, y, z])
            added_idx.add((x + 1, y, z))
        if y + 1 < Y and (x, y + 1, z) not in added_idx:
            heapq.heappush(Q, [-(A[x] + B[y + 1] + C[z]), x, y + 1, z])
            added_idx.add((x, y + 1, z))
        if z + 1 < Z and (x, y, z + 1) not in added_idx:
            heapq.heappush(Q, [-(A[x] + B[y] + C[z + 1]), x, y, z + 1])
            added_idx.add((x, y, z + 1))


def __starting_point():
    main()


__starting_point()
