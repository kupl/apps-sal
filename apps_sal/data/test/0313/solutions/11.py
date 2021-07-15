#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input())
A = list(map(int,input().split()))

attends = 0
i = 0
while i < n:
    if A[i] == 1:
        attends += 1
    else:
        if 0 < i < n - 1 and A[i-1] == 1  and A[i+1] == 1:
            attends += 2
            i += 1
    i += 1
print(attends)

