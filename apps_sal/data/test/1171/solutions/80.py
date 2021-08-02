from heapq import heapify, heappop, heappush
from collections import deque
import sys
sys.setrecursionlimit(10 ** 9)
# input = sys.stdin.readline    ####
def int1(x): return int(x) - 1
def II(): return int(input())
def MI(): return list(map(int, input().split()))
def MI1(): return list(map(int1, input().split()))
def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def MS(): return input().split()
def LS(): return list(input())
def LLS(rows_number): return [LS() for _ in range(rows_number)]
def printlist(lst, k=' '): print((k.join(list(map(str, lst)))))


INF = float('inf')
# from math import ceil, floor, log2
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# import numpy as np
# from numpy import cumsum  # accumulate


def solve():
    N, K = MI()
    V = LI()
    max_iter = min(N, K)
    ans = 0
    for a in range(max_iter + 1):
        left = V[:a]
        for b in range(0, max_iter - a + 1):
            right = V[-b:] if b != 0 else []
            k = K - a - b
            # print(a, b, k)
            # print(left, right)
            lst = sorted(left + right)
            # print(lst)
            sm = sum(lst)
            l = len(lst)
            for kk in range(1, k + 1):
                if kk < l:
                    tmp = lst[kk - 1]
                    if tmp >= 0: break
                    sm -= tmp
                    # print(tmp)
                else:
                    break
            ans = max(ans, sm)
    print(ans)


def __starting_point():
    solve()


__starting_point()
