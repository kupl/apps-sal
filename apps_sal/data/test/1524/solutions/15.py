#!/usr/bin/env python3

#import
#import math
#import numpy as np
S = input()
ls = len(S)

li = [0] * ls

r = 0
l = 0

for i in range(ls):
    if S[i] == "L":
        l += 1
    else:
        if l == 0:
            r += 1
        else:
            li[i - l] += r // 2 + (l + 1) // 2
            li[i - l - 1] += (r + 1) // 2 + l // 2

            r = 1
            l = 0

li[ls - l] += r // 2 + (l + 1) // 2
li[ls - l - 1] += (r + 1) // 2 + l // 2

li = [str(li[i]) for i in range(ls)]

print((" ".join(li)))



