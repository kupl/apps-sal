from math import floor, sqrt, factorial, hypot, log
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from random import randint
from fractions import gcd
from copy import deepcopy
from heapq import heappop, heappush, heappushpop
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def ceil(a, b):
    return (a + b - 1) // b


inf = float('inf')
mod = 10 ** 9 + 7


def pprint(*A):
    for a in A:
        print(*a, sep='\n')


def INT_(n):
    return int(n) - 1


def MI():
    return map(int, input().split())


def MF():
    return map(float, input().split())


def MI_():
    return map(INT_, input().split())


def LI():
    return list(MI())


def LI_():
    return [int(x) - 1 for x in input().split()]


def LF():
    return list(MF())


def LIN(n: int):
    return [I() for _ in range(n)]


def LLIN(n: int):
    return [LI() for _ in range(n)]


def LLIN_(n: int):
    return [LI_() for _ in range(n)]


def LLI():
    return [list(map(int, l.split())) for l in input()]


def I():
    return int(input())


def F():
    return float(input())


def ST():
    return input().replace('\n', '')


def main():
    N = I()
    A = sorted(LI())
    MAX = 10 ** 6
    divible = [False] * (MAX + 1)
    ans = 0
    for (i, a) in enumerate(A):
        if i + 1 < N and A[i + 1] == a or divible[a]:
            pass
        else:
            ans += 1
        b = a
        if not divible[a]:
            while b <= MAX:
                divible[b] = True
                b += a
    print(ans)


def __starting_point():
    main()


__starting_point()
