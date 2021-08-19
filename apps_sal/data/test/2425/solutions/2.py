from sys import setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import defaultdict, Counter
from bisect import bisect
setrecursionlimit(10 ** 7)


def read():
    return int(input())


def reads():
    return [int(x) for x in input().split()]


def largest_factor(x):
    ans = 1
    for y in range(2, 2 ** 13):
        if x % y == 0:
            ans = max(ans, x // y)
    return ans


def solve(a):
    highest_bit = max((1 << i for i in range(30) if 1 << i & a > 0))
    M = highest_bit * 2 - 1
    return M if a != M else largest_factor(M)


q = read()
for _ in range(q):
    a = read()
    print(solve(a))
