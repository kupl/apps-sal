#!/usr/bin python3
# -*- coding: utf-8 -*-

N, M = list(map(int, input().split()))
vals = [[] for _ in range(8)]
for _ in range(N):
    a, b, c = list(map(int,input().split()))
    vals[0].append( a+b+c)
    vals[1].append( a+b-c)
    vals[2].append( a-b+c)
    vals[3].append( a-b-c)
    vals[4].append(-a+b+c)
    vals[5].append(-a+b-c)
    vals[6].append(-a-b+c)
    vals[7].append(-a-b-c)
ret = 0
for val in vals:
    val.sort(reverse = True)
    ret = max(ret, sum(val[:M]))
print(ret)

