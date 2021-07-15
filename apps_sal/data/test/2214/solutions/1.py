from collections import *
from sys import stdin, stderr
def rl():
    return [int(w) for w in stdin.readline().split()]

n, m = rl()
if n > 3:
    print(-1)
    return
if n < 2:
    print(0)
    return
a = [[int(c) for c in stdin.readline().rstrip()] for _ in range(n)]
if n == 2:
    a.append(a[0])
r = n * m
for target in range(4):
    total = 0
    for a0, a1, a2 in zip(*a):
        if a0 ^ a1 != target & 1 or a1 ^ a2 != target >> 1:
            total += 1
        target ^= 3
    if total < r:
        r = total
print(r)

