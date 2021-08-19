#!/usr/bin/env python3
from sys import stdin, stdout


def readint():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()


n, t, k, d = readint()

tt = (n // k) * t
if n % k:
    tt += t

if tt > d + t:
    print("YES")
else:
    print("NO")
