from math import floor, sqrt, factorial, hypot, log
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from random import randint
from fractions import gcd
from copy import deepcopy
from heapq import heappop, heappush, heappushpop
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def ceil(a, b): return (a + b - 1) // b


inf = float('inf')
mod = 10**9 + 7


def pprint(*A):
    for a in A:
        print(*a, sep='\n')


def INT_(n): return int(n) - 1
def MI(): return map(int, input().split())
def MF(): return map(float, input().split())
def MI_(): return map(INT_, input().split())
def LI(): return list(MI())
def LI_(): return [int(x) - 1 for x in input().split()]
def LF(): return list(MF())
def LIN(n: int): return [I() for _ in range(n)]
def LLIN(n: int): return [LI() for _ in range(n)]
def LLIN_(n: int): return [LI_() for _ in range(n)]
def LLI(): return [list(map(int, l.split())) for l in input()]
def I(): return int(input())
def F(): return float(input())
def ST(): return input().replace('\n', '')


def main():
    N = I()
    A = LI()
    MAX = max(A)
    MIN = min(A)
    print(2 * N - 1)
    if abs(MAX) < abs(MIN):
        min_idx = A.index(MIN) + 1
        for i in range(1, N + 1):
            print(min_idx, i)
        for i in range(2, N + 1)[::-1]:
            print(i, i - 1)
    else:
        max_idx = A.index(MAX) + 1
        for i in range(1, N + 1):
            print(max_idx, i)
        for i in range(1, N):
            print(i, i + 1)


def __starting_point():
    main()


__starting_point()
