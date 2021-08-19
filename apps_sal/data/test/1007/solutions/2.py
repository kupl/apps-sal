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
created by shhuan at 2017/12/2 22:09

"""

K, P = map(int, input().split())

ans = 0
for v in range(1, K + 1):
    x = str(v)
    x = x + x[::-1]
    x = int(x)
    ans += x
    ans %= P
print(ans)
