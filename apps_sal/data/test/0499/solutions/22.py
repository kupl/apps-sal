#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


def pr(d, k):
    ans = []
    for i in d.keys():
        if d[i] == k:
            ans = i
    return ans


n = int(input())
a = list(input())

start = time.time()

d = {'R': 0, 'G': 0, 'B': 0}

for i in a:
    d[i] += 1

b = list(set(a))

if len(b) == 1:
    ans = b[0]
elif len(b) == 2:
    if d[b[0]] == 1 and d[b[1]] == 1:
        ans = pr(d, 0)
    elif d[b[0]] == 1:
        ans = b[0] + pr(d, 0)
    elif d[b[1]] == 1:
        ans = b[1] + pr(d, 0)
    else:
        ans = 'BGR'
else:
    ans = 'BGR'

for i in sorted(ans):
    print(i, end='')
print()

finish = time.time()
#print(finish - start)
