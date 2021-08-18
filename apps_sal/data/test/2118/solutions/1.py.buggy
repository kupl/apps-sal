# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/14 15:30

"""

n, k = map(int, input().split())

if k & 1 == 0 or k > 2 * n - 1:
    print(-1)
else:
    a = [0] * n
    gs = (k - 1) // 2

    def unsort(l, r, v):
        if l == r - 1:
            a[l] = v
        else:
            nonlocal gs
            if gs > 0:
                gs -= 1
                mid = (l + r) // 2
                unsort(l, mid, v + r - mid)
                unsort(mid, r, v)
            else:
                for i in range(r - l):
                    a[l + i] = v + i

    unsort(0, n, 1)

    print(' '.join([str(x) for x in a]))
