# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 09:32:18 2018

@author: yanni
"""

n, L = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
size = [2**p for p in range(n)]
for index in range(n):
    if (index > 0):
        c[index] = min(c[index], c[index - 1] * 2)
for index in range(n):
    if (index > 0):
        temp = n - 1 - index
        c[temp] = min(c[temp], c[temp + 1])
poss = []
base = 0
maxindex = 0
while (size[maxindex] < L and maxindex < n - 1):
    maxindex += 1
if (size[maxindex] < L):
    base = (L // size[maxindex]) * c[maxindex]
    L = L % size[maxindex]
if (L == 0):
    print(base)
else:
    poss.append(base + c[maxindex])
    curr = base
    while (L > 0):
        while (size[maxindex] >= 2 * L):
            maxindex -= 1
        poss.append(curr + c[maxindex])
        if (maxindex == 0):
            curr += c[0]
            L = 0
        else:
            L -= size[maxindex - 1]
            curr += c[maxindex - 1]
    poss.append(curr)
    print(min(poss))
