# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2020/1/14 22:37

"""


def solve(N, D):
    X = int(math.sqrt(D))

    for x in range(max(0, X-10), min(N, X+10) + 1):
        if x + int(math.ceil(D / (x + 1))) <= N:
            return True
    return False


T = int(input())
ans = []
for ti in range(T):
    N, D = map(int, input().split())
    ans.append(solve(N, D))

print('\n'.join(['YES' if v else 'NO' for v in ans]))
