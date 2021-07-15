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
# from collections import deque, defaultdict
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np    # cumsum
# from bisect import bisect_left, bisect_right

def solve():
    X, Y, A, B, C = MI()
    # R = LI()
    # G = LI()
    # T = LI()
    L = []
    for r in LI():
        L.append((r, 'R'))
    for g in LI():
        L.append((g, 'G'))
    for t in LI():
        L.append((t, 'T'))
    L = sorted(L, reverse=True)
    # print(L)

    ans = 0
    left = X + Y
    for n, c in L:
        if c == 'R':
            if X > 0:
                ans += n
                X -= 1
            else:
                continue
        elif c == 'G':
            if Y > 0:
                ans += n
                Y -= 1
            else:
                continue
        else:
            ans += n

        left -= 1
        if left == 0:
            print(ans)
            return

def __starting_point():
    solve()


__starting_point()
