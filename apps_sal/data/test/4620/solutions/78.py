#!/usr/bin/env python3
import sys
import math
sys.setrecursionlimit(10**6)
n = int(input())

csf = [list(map(int, input().split())) for i in range(n-1)]

for i in range(n-1):
    csf_tmp = csf[i:]

    c, s, f = csf_tmp[0]

    t = c+s
    for j in range(1, len(csf_tmp)):
        c, s, f = csf_tmp[j]

        if t <= s:
            t = s
        else:
            mod = (t-s) % f
            if mod != 0:
                t += f-mod
        # print(t)
        t += c
        # print(t)
    print(t)
    # print()
print((0))

