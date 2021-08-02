from heapq import heapify, heappush, heappop
from collections import Counter, defaultdict, deque, OrderedDict
from sys import setrecursionlimit, maxsize
from bisect import bisect_left, bisect, insort_left, insort
from math import ceil, log, factorial, hypot, pi
from fractions import gcd
from copy import deepcopy
from functools import reduce
from operator import mul
from itertools import product, permutations, combinations, accumulate, cycle
from string import ascii_uppercase, ascii_lowercase, ascii_letters, digits, hexdigits, octdigits

prod = lambda l: reduce(mul, l)
prodmod = lambda l, mod: reduce(lambda x, y: mul(x, y) % mod, l)
argmax = lambda l: l.index(max(l))
argmin = lambda l: l.index(min(l))


def read_list(t): return [t(x) for x in input().split()]
def read_line(t): return t(input())
def read_lines(t, N): return [t(input()) for _ in range(N)]


H = read_list(int)

n = H[3]
ans = 0
left, right = H[4], H[2]
while left > 0 and right > 0:
    left -= 1
    right -= 1
    ans += 2 * n + 1
    n += 1

if left == 0:
    left = H[5]
    while right > 0:
        ans += 2 * n
        right -= 1
        left -= 1
    right = H[1]

else:
    right = H[1]
    while left > 0:
        ans += 2 * n
        right -= 1
        left -= 1
    left = H[5]

while H[0] < n:
    ans += 2 * n - 1
    n -= 1
print(ans)
