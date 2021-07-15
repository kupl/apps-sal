#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n, m = list(map(int, input().split()))

x = m
y = n-m

ans = (1900*x+100*y)*2**x

print(ans)

