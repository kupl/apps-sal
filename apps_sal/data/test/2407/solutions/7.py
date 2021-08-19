#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import math

q = int(input())
ans = []
start = time.time()

for i in range(q):
    (n, r) = (int(j) for j in input().split())
    x = [int(j) for j in input().split()]
    x = list(set(x))
    x.sort()
    p = [0 for j in range(len(x))]
    for j in range(len(x)):
        p[j] = min(math.ceil(x[j] / r), len(x) - j)
    ans.append(max(p))

for i in range(q):
    print(ans[i])
finish = time.time()
#print(finish - start)
