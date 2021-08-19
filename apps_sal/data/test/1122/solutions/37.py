from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque, Counter
from operator import mul
import copy
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import heapq

n, m = list(map(int, input().split()))

p = m // 2
for i in range(p):
    print((p - i, p + 2 + i))

q = m // 2 + 1
if m % 2 == 1:
    for i in range(q):
        print((m + q - i, m + q + i + 1))
else:
    for i in range(q - 1):
        print((m + q - i, m + q + i + 1))
