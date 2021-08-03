#!/usr/bin/env python3
import os
from sys import stdin, stdout


def solve(tc):
    n = int(stdin.readline().strip())
    seq = list(map(int, stdin.readline().split()))
    seq = sorted(seq)

    base = seq[0]
    for i in range(1, n):
        if seq[i] - base > 1:
            print("NO")
            return
        base = seq[i]
    print("YES")


tcs = 1
tcs = int(stdin.readline().strip())
tc = 1
while tc <= tcs:
    solve(tc)
    tc += 1
