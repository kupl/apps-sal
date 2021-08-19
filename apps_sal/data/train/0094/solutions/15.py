import os
import sys
import io
GANS = []
t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    li = [int(i) for i in input().split()]
    d1 = {}
    d2 = {}
    col = []
    for i in li:
        if d1.get(k - i, 0) > d2.get(k - i, 0):
            d2[i] = d2.get(i, 0) + 1
            col.append(1)
        else:
            d1[i] = d1.get(i, 0) + 1
            col.append(0)
    print(*col)
