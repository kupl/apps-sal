#!/usr/bin/env python3

A, B, C = list(map(int, input().split()))
if A == B:
    print(C)
elif A == C:
    print(B)
else:
    print(A)
