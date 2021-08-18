import sys
import heapq
import functools
import collections
import math
import random
from collections import Counter, defaultdict


def solve(lst):
    console("----- solving ------")

    maxres = lst[0] * lst[1] * lst[2] * lst[3] * lst[4]

    if 0 in lst:
        maxres = max(maxres, 0)

    positives = sorted([a for a in lst if a >= 0])[::-1]
    negatives = sorted([a for a in lst if a < 0])

    if len(positives) >= 5 and len(negatives) >= 0:
        maxres = max(maxres, positives[0] * positives[1] * positives[2] * positives[3] * positives[4])

    if len(positives) >= 3 and len(negatives) >= 2:
        maxres = max(maxres, positives[0] * positives[1] * positives[2] * negatives[0] * negatives[1])

    if len(positives) >= 1 and len(negatives) >= 4:
        maxres = max(maxres, positives[0] * negatives[0] * negatives[1] * negatives[2] * negatives[3])

    if len(negatives) >= 5:
        maxres = max(maxres, negatives[-1] * negatives[-2] * negatives[-3] * negatives[-4] * negatives[-5])

    return maxres


def console(*args):
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return


for case_num in range(int(input())):

    k = int(input())

    lst = list(map(int, input().split()))

    res = solve(lst)

    print(res)
