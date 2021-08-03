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

n, p = list(map(int, input().split()))
s = input()

ans = 0

if p == 2 or p == 5:
    for i in range(n):
        a = int(s[n - 1 - i])
        if a % p == 0:
            ans += n - i

else:
    d = {0: 1}
    c = 0
    for i in range(n):
        c += (pow(10, i, p) * int(s[n - 1 - i])) % p
        c %= p
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    for dd in list(d.values()):
        ans += dd * (dd - 1) // 2

print(ans)
