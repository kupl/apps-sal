#!/usr/bin/env python3

#import
#import math
#import numpy as np
A, B, X = list(map(int, input().split()))

if A + B > X:
    print((0))
    return

t = 1
for i in range(1, 20):
    t *= 10
    if A * t + B * i > X:
        break

def is_ok(arg):
    a = len(str(arg))
    return A * arg + B * a <= X

def meguru_bisect(ok, ng):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print((meguru_bisect(min(t // 10, 10**8), min(t + 1, 10**9 + 1))))





