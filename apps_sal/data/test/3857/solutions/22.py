#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
n = int(input())
box = [int(x) for x in input().split()]
box.sort()
k = 0
for i in range(n):
    if k * (box[i] + 1) <= i:
        k += 1
print(k)
