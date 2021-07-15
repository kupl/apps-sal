import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline    ####
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
INF = float('inf')
# from bisect import bisect_left, bisect_right
# from heapq import heapify, heappop, heappush
from math import ceil, floor, log2, log, sqrt
from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
from collections import deque, defaultdict
from pprint import pprint
# import numpy as np    # cumsum

def solve():
    N, K = MI()

    print((ceil((N-1) / (K-1))))


def __starting_point():
    solve()


__starting_point()
