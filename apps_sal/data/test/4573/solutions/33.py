#!/usr/bin/env python
import sys 
import copy
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
xx = sorted(x)

l = xx[(n-1)//2]
r = xx[n//2]
mid = (l+r)/2

for i in range(n):
    if x[i] >= mid:
        print(l)
    else:
        print(r)

