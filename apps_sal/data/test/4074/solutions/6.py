import sys
import heapq
import random
import collections
from functools import reduce


def all_divisors(n):
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


def solve(n, k):
    lst = all_divisors(n)
    lst = sorted(list(lst))
    for i in lst[::-1]:
        if i <= k:
            return n // i
    return n


def console(*args):
    print('\x1b[36m', *args, '\x1b[0m', file=sys.stderr)
    return


for case_num in range(int(input())):
    (n, k) = list(map(int, input().split()))
    res = solve(n, k)
    print(res)
