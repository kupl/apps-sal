from pprint import pprint
from collections import deque, defaultdict
from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
from math import ceil, floor, log2, log, sqrt
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def int1(x):
    return int(x) - 1


def II():
    return int(input())


def MI():
    return list(map(int, input().split()))


def MI1():
    return list(map(int1, input().split()))


def LI():
    return list(map(int, input().split()))


def LI1():
    return list(map(int1, input().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def MS():
    return input().split()


def LS():
    return list(input())


def LLS(rows_number):
    return [LS() for _ in range(rows_number)]


INF = float('inf')


def solve():
    (N, K) = MI()
    A = LI()
    print(ceil((N - 1) / (K - 1)))


def __starting_point():
    solve()


__starting_point()
