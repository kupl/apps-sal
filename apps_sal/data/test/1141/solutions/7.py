# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/12/2 22:05

"""


N, M = map(int, input().split())

S = list(input())

for i in range(M):
    l, r, c1, c2 = input().split()
    l, r = int(l), int(r)

    for j in range(l-1, r):
        if S[j] == c1:
            S[j] = c2

print("".join(S))
