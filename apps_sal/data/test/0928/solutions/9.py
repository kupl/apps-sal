from collections import Counter, deque
import itertools
import sys
import math
from math import gcd, pi, sqrt
INF = float("inf")

sys.setrecursionlimit(10**6)
def i_input(): return int(input())
def i_map(): return list(map(int, input().split()))
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
    n, k = i_map()
    a = i_list()

    X = [0] + list(itertools.accumulate(a))

    ans = 0
    from bisect import bisect_left
    for x in X:
        i = bisect_left(X, k + x)
        if i == n + 1:
            if X[-1] - x >= k:
                ans += 1
        else:
            ans += n - i + 1

    print(ans)


def __starting_point():
    main()


__starting_point()
