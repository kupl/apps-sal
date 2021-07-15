from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter
from operator import mul
import copy
# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import heapq

n = int(input())

aa = []
bb = []
for i in range(n):
    a , b = list(map(int, input().split()))

    aa.append(a)
    bb.append(b)

aa.sort()
bb.sort()

if n % 2 == 0:
    m_a = (aa[n // 2 - 1] + aa[n // 2])
    m_b = (bb[n // 2 - 1] + bb[n // 2])

    print(m_b - m_a+1)
    return

else:
    median_a = aa[n // 2]
    median_b = bb[n // 2]

    print(median_b-median_a+1)
    return
