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
created by shhuan at 2017/11/9 23:24

"""


N, K = list(map(int, input().split()))

if K == 1:
    print(1)
elif K == 2:
    print(1 + N * (N - 1) // 2)
elif K == 3:
    print(1 + N * (N - 1) // 2 + N * (N - 1) * (N - 2) // 3)
elif K == 4:
    print(1 + N * (N - 1) // 2 + N * (N - 1) * (N - 2) // 3 + 3 * N * (N - 1) * (N - 2) * (N - 3) // 8)
