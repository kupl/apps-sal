#!/usr/bin/env python3
from sys import stdin, stdout

def rint():
    return map(int, stdin.readline().split())
#lines = stdin.readlines()

n = int(input())
f = list(rint())
f = [-1] + f
for i in range(1,n+1):
    a = i
    b = f[a]
    c = f[b]
    d = f[c]
    if a == d:
        print("YES")
        return

print("NO")
