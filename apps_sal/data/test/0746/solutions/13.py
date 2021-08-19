#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import math

(a, b) = (int(i) for i in input().split())
n = int(input())
t = float('Inf')

for i in range(n):
    (x, y, v) = (int(i) for i in input().split())
    new_t = math.sqrt((x - a) * (x - a) + (y - b) * (y - b)) / v
    if new_t < t:
        t = new_t

start = time.time()

print(t)
finish = time.time()
#print(finish - start)
