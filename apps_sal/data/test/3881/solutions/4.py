#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

pat = {}

(n, q) = (int(i) for i in input().split())
for i in range(q):
    (a, b) = [i for i in input().split()]
    if b in list(pat.keys()):
        pat[b].append(a)
    else:
        pat[b] = [a]

start = time.time()

str = ['a']
for i in range(n - 1):
    newstr = []
    for j in range(len(str)):
        l = str[j][0]
        if l in list(pat.keys()):
            for k in pat[l]:
                newstr.append(k + str[j][1:])

    str = newstr
    if len(str) == 0:
        break

print(len(str))
finish = time.time()
#print(finish - start)
