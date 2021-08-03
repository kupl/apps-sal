import numpy as np    # cumsum
from math import ceil, floor, log2
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
# from collections import deque, defaultdict
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# from bisect import bisect_left, bisect_right


def solve():
    N = II()
    A = LI()
    for i in range(N):
        A[i] = A[i] - (i + 1)
    med = int(np.median(A))
    # print(med)
    ans = 0
    for a in A:
        ans += abs(a - med)
    print(ans)


def __starting_point():
    solve()


__starting_point()
