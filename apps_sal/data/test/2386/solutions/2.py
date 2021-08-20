from sys import stdin, setrecursionlimit
import bisect
import collections
import copy
import heapq
import itertools
import math
import string
setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 1000000007


def input():
    return stdin.readline().strip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] -= i + 1
    a.sort()
    ans = 0
    b = a[n // 2]
    for x in a:
        ans += abs(x - b)
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
