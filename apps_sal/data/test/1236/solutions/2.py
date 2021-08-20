import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
from itertools import chain, dropwhile, permutations, combinations
from collections import defaultdict, deque


def VI():
    return list(map(int, input().split()))


def main(n, k, a):
    now = sum(a)
    even = sum([x % 2 == 0 for x in a])
    odd = sum([x % 2 == 1 for x in a])
    d = n - k
    D = 'Daenerys'
    S = 'Stannis'
    if n == k:
        ans = [S, D][now % 2 == 0]
    elif d % 2 == 0:
        if k % 2 == 0:
            ans = D
        elif even <= d // 2:
            ans = S
        else:
            ans = D
    elif k % 2 == 0:
        if odd <= d // 2 or even <= d // 2:
            ans = D
        else:
            ans = S
    elif odd <= d // 2:
        ans = D
    else:
        ans = S
    print(ans)


def main_input(info=0):
    (n, k) = VI()
    a = VI()
    main(n, k, a)


def __starting_point():
    main_input()


__starting_point()
