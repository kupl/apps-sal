from heapq import heapify, heappop, heappush
from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product
from collections import deque
from math import ceil, floor, log2
import sys
sys.setrecursionlimit(10 ** 6)
def int1(x): return int(x) - 1
def II(): return int(input())


def MI(): return list(map(int, input().split()))
def MI1(): return list(map(int1, input().split()))


def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def SI(): return input().split()


def printlist(lst, k='\n'): print((k.join(list(map(str, lst)))))


INF = float('inf')


def solve():
    n, k = MI()
    A = LI()
    sm = sum(A)

    div = []
    for i in range(1, int(pow(sm, 0.5)) + 1):
        if sm % i:
            continue
        div.append(i)
        if i != sm // i:
            div.append(sm // i)
    ans = 1
    for d in div:
        R = [a % d for a in A]
        R.sort()
        plus = 0
        minus = 0
        for r in R:
            plus += d - r
        for r in R:
            minus += r
            plus -= d - r
            if minus == plus and plus <= k:
                ans = max(ans, d)
    print(ans)


def __starting_point():
    solve()


__starting_point()
