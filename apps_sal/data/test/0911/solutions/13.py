#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

#   = input()
#   = int(input())

#() = (i for i in input().split())
#   = [i for i in input().split()]

(n, c) = (int(i) for i in input().split())
p = [int(i) for i in input().split()]
t = [int(i) for i in input().split()]

start = time.time()

tnow = 0
T = sum(t)

sl = 0
sr = 0

for i in range(n):
    sr += max(0, p[i] - c * (T - tnow))
    tnow += t[i]
    sl += max(0, p[i] - c * tnow)

if sl > sr:
    print('Limak')
elif sl == sr:
    print('Tie')
else:
    print('Radewoosh')

finish = time.time()
#print(finish - start)
