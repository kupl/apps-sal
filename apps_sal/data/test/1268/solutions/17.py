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
created by shhuan at 2017/11/17 22:35

"""

N = int(input())

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

left = sum(A)
B.sort(reverse=True)

if left <= B[0] + B[1]:
    print("YES")
else:
    print("NO")
