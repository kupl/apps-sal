#!/usr/bin python3
# -*- coding: utf-8 -*-

from collections import Counter

n, m = map(int, input().split())
a = [int(i)%m for i in input().split()]
for i in range(1,n):
    a[i] = (a[i] + a[i-1])%m
a = [0] + a
a = Counter(a)
ret = 0
for i, v in a.items():
    ret += v*(v-1)//2
print(ret)
