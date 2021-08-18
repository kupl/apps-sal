#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())

if n == 1:
    print((1))
    return

a = 2
b = 1
now = 3
count = 2
for i in range(2, n):
    a = b
    b = now
    now = a + b

print(now)
