#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import math

n       = int(input())
m       = int(input())
a       = []

for i in range(n):
    a.append(int(input()))

start   = time.time()

max_now = max(a)
sum     = 0

for i in range(n):
    sum += max_now-a[i]

ans_max = max_now+m
if sum >= m:
    ans_min = max_now
else:
    ans_min=max_now+math.ceil((m-sum)/n)

print(ans_min, ans_max)
finish = time.time()
#print(finish - start)

