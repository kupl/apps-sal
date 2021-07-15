#!/usr/bin/env python3

N, X = list(map(int, input().split()))
A = set(map(int, input().split()))

out = X - sum(1 for n in A if n < X)
if X in A:
    out += 1

print(out)


