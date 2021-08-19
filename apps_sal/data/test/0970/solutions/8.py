#!/usr/bin/env python3

n = int(input().strip())
pis = list(map(int, input().strip().split()))

pis.sort()

w1 = sum(abs(2 * i + 1 - p) for i, p in enumerate(pis))
w2 = sum(abs(2 * i + 2 - p) for i, p in enumerate(pis))

print(min(w1, w2))
