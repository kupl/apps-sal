#!/usr/bin/env python3
import sys

def rint():
    return list(map(int, sys.stdin.readline().split()))
#lines = stdin.readlines()

n = int(input())

ans = 0
for i in range(2,n):
    ans += i*(i+1)

print(ans)

