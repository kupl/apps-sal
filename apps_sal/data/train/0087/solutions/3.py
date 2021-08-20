import sys
import heapq
import functools
import collections
import math
import random
from collections import Counter, defaultdict


def solve(m, d, w):
    console('----- solving ------')
    a = int(w / math.gcd(w, 1 - d))
    b = min(m, d)
    console(a, b)
    return (1 + b // a) * (b + b % a) // 2 - b


def console(*args):
    print('\x1b[36m', *args, '\x1b[0m', file=sys.stderr)
    return


for case_num in range(int(input())):
    (m, d, w) = list(map(int, input().split()))
    res = solve(m, d, w)
    print(res)
