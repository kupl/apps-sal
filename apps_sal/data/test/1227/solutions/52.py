from math import ceil, floor, factorial, gcd, sqrt, log2, cos, sin, tan, acos, asin, atan, degrees, radians, pi, inf, comb
from itertools import accumulate, groupby, permutations, combinations, product, combinations_with_replacement
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
from operator import itemgetter
from heapq import heapify, heappop, heappush
from queue import Queue, LifoQueue, PriorityQueue
from copy import deepcopy
from time import time
from functools import reduce
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def MAP1(): return [int(x) - 1 for x in input().split()]
def LIST(): return list(MAP())
def LIST1(): return list(MAP1())


def solve(n, k, m):
    ans = 0
    for i in range(k, m):
        if k == 1:
            ans += 9
        else:
            ans += pow(9, k) * comb(i - 1, k - 1)
    if k == 1:
        ans += int(n[0])
    elif k == 2:
        ans += (int(n[0]) - 1) * pow(9, k - 1) * comb(m - 1, k - 1)
        j = 1
        while j < m and n[j] == '0':
            j += 1
        if j < m:
            ans += int(n[j]) + pow(9, k - 1) * comb(m - 1 - j, k - 1)
    else:
        while m >= k and n.count('0') > m - k:
            n = str(int(n) - 1)

        if m > len(n):
            print(ans)
            return ans

        m = len(n)
        a = []
        for i in range(m):
            if len(a) < 3 and n[i] != '0':
                a.append(i)

        if len(a) == 3:
            ans += 1 + int(n[a[2]]) - 1 + 9 * comb(m - 1 - a[2], 1)
            ans += (int(n[a[1]]) - 1) * 9 * comb(m - 1 - a[1], 1) + 9 * 9 * comb(m - 1 - a[1], 2)
            ans += (int(n[a[0]]) - 1) * 9 * 9 * comb(m - 1 - a[0], 2)
    print(ans)
    return ans


def solve2(n, k, m):
    ans = 0
    for i in range(1, int(n) + 1):
        if len(str(i)) - str(i).count('0') == k:
            ans += 1
    print(ans)
    return ans


def __starting_point():
    n = input()
    k = INT()
    m = len(n)

    solve(n, k, m)


__starting_point()
