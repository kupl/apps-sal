#!/usr/bin/env python3
N, K = list(map(int, input().split()))
L = sorted(list(map(int, input().split())))
print((sum(L[-K:])))
