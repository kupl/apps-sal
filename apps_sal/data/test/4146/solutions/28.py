#!/usr/bin/env python3

# import
#import math
#import numpy as np
n = int(input())
V = list(map(int, input().split()))

even = {0: 0}
odd = {0: 0}

for i in range(n):
    v = V[i]
    if i % 2 == 0:
        if v in even:
            even[v] += 1
        else:
            even[v] = 1
    else:
        if v in odd:
            odd[v] += 1
        else:
            odd[v] = 1

omax = 0
emax = 0
onext = 0
enext = 0

for e in even:
    if even[e] > even[emax]:
        if even[emax] > even[enext]:
            enext = emax
        emax = e
    elif even[e] > even[enext]:
        enext = e

for o in odd:
    if odd[o] > odd[omax]:
        if odd[omax] > odd[onext]:
            onext = omax
        omax = o
    elif odd[o] > odd[onext]:
        onext = o

if omax != emax:
    print((n - even[emax] - odd[omax]))
else:
    print((n - even[emax] - odd[omax] + min(even[emax] - even[enext], odd[omax] - odd[onext])))
