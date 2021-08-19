import sys
import heapq
import functools
import collections
import math
import random
from collections import Counter, defaultdict


def solve(arr, brr):
    console('----- solving ------')
    for candidate in range(512):
        for a in arr:
            for b in brr:
                if a & b | candidate == candidate:
                    break
            else:
                break
        else:
            return candidate


def console(*args):
    print('\x1b[36m', *args, '\x1b[0m', file=sys.stderr)
    return


_ = list(map(int, input().split()))
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
res = solve(arr, brr)
print(res)
