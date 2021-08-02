#!/usr/bin/env python3

import sys

input = iter(sys.stdin.read().splitlines()).__next__

sys.setrecursionlimit(10000)

A = list(map(int, input().split()))

for i in range(len(A)):
    if A[i] == 0:
        print((i + 1))
