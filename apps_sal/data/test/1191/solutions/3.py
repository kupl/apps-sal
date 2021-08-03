#!/usr/bin/env python3

from heapq import heappop, heappush

[n, k] = list(map(int, input().strip().split()))
pis = list(map(int, input().strip().split()))
cis = list(map(int, input().strip().split()))

res = [0 for _ in range(n)]
nis = list(range(n))
nis.sort(key=lambda i: pis[i])

hc = []
l = 0
sc = 0

for i in nis:
    sc += cis[i]
    res[i] = sc
    heappush(hc, cis[i])
    if l == k:
        sc -= heappop(hc)
    else:
        l += 1

print(' '.join(map(str, res)))
