#import sys
import pprint
from collections import defaultdict
from functools import lru_cache
import copy
from fractions import Fraction
import heapq
import itertools
from collections import deque
import math
MOD = 10 ** 9 + 7
INFI = 10**10
#input = sys.stdin.readline
#import bisect

# oo=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# ko=list("abcdefghijklmnopqrstuvwxyz")


def sosuhante(n):
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True


def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


def kingaku(a, b, n):
    keta = len(str(n))
    return a * n + b * keta


def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default

#    h,w,a,b = map(int, input().split())
#    c = [[0 for j in range(n)] for i in range(n)]


def ret(a):
    c = [None] * (len(a) - 1)
    if len(a) == 1:
        return a[0]
    elif len(a) == 0:
        return 0
    for i in range(1, len(a)):
        c[i - 1] = abs(a[i] - a[i - 1])
    return ret(c)


def soinsubunkai(n):
    a = []
    i = 1
    while i * i <= n:
        if n % i == 0 and i != 1:
            a.append(i)
            n = n // i

        if n % i != 0 or i == 1:
            i += 1
    nokori = [n]
    return a + nokori


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    stack = []
    visited = [0 for _ in range(n + 1)]

    zones = 0
    count = 0

    def DFS():
        c = 1
        while True:
            if len(stack) == 0:
                break
            s = stack.pop()
            if visited[s] == 0:
                for i in graph[s]:
                    if visited[i] == 0:
                        stack.append(i)

                visited[s] = 1
                c += 1
            if len(stack) == 0:
                break
        return c
    for i in range(1, n + 1):
        if visited[i] == 0:
            visited[i] = 1
            for j in graph[i]:
                stack.append(j)
            if len(stack) > 0:
                count += DFS()
                zones += 1
        else:
            continue

#    print(n,count,zones)
    print(n - count + zones)


def __starting_point():

    main()


__starting_point()
