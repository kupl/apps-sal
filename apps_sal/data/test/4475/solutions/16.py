import sys
import math
import heapq
import collections
import itertools
import bisect
sys.setrecursionlimit(101000)


def solve(a, b, x, y, n):
    diffa = a - x
    diffb = b - y
    first = min(diffb, n)
    b -= first
    n -= first
    second = min(diffa, n)
    a -= second
    n -= second
    return a * b


t = int(input())
for _ in range(t):
    # n = int(input())
    a, b, x, y, n = map(int, input().split())
    # a = list(map(int, input().split()))
    print(min(solve(a, b, x, y, n), solve(b, a, y, x, n)))
