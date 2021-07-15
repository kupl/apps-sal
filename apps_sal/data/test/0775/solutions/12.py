#!/usr/bin/env python3
from sys import stdin,stdout


def ri():
    return list(map(int, stdin.readline().split()))

n, m, k = ri()
h = [0 for i in range(n+1)]
hh = list(ri())
for i in range(m):
    h[hh[i]] = 1
p = 1
for i in range(k):
    if h[p] == 1:
        print(p)
        return
    a, b = ri()
    if p in [a, b]:
        if a == p:
            p = b
        else:
            p = a

print(p)



