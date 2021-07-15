#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calc(p, t):
    return max(3*p//10, p - p//250 * t)

(a,b,c,d) = list(map(int, input().split()))
m = calc(a, c)
v = calc(b, d)

ret = ""
if m > v:
    ret = "Misha"
elif v > m:
    ret = "Vasya"
else:
    ret = "Tie"

print(ret)


