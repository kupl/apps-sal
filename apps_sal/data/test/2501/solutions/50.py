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
a = list(map(int, input().split()))

p = [i-a[i] for i in range(n)]
q = [a[i]+i for i in range(n)]

pp = Counter(p)
qq = Counter(q)

ans = 0
for d in list(pp.items()):
    ans += d[1] * qq[d[0]]

print(ans)







