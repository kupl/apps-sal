#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

a, b, c, d = list(map(int, input().split()))

e = a+b
f = c+d
if e > f:
    print("Left")
if e == f:
    print("Balanced")
if e < f:
    print("Right")

