#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

n   = int(input())
N   = {}
P   = {}

for i in range(n):
    buf = input().split()
    x   = float(buf[0])
    a   = int (buf[1])
    if x < 0:
        N[-x] = a
    else:
        P[x] = a

start = time.time()

if len(N) > len(P):
    buf = [ N[i] for i in sorted(N.keys()) ]
    ans = sum(P.values()) + sum(buf[:len(P)+1])
else:
    buf = [ P[i] for i in sorted(P.keys()) ]
    ans = sum(N.values()) + sum(buf[:len(N)+1])
print(ans)
finish = time.time()
#print(finish - start)

