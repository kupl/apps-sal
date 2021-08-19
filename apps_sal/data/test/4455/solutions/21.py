#!/usr/bin/env python3
from sys import stdin, stdout
from bisect import bisect_left


def rint():
    return map(int, stdin.readline().split())
#lines = stdin.readlines()


n, k = rint()
r = list(rint())
q = [0 for i in range(n)]

for i in range(k):
    x, y = rint()
    x -= 1
    y -= 1
    if r[x] > r[y]:
        q[x] += 1
    elif r[y] > r[x]:
        q[y] += 1

ans = [-1 for i in range(n)]
r_sorted = r[:]
r_sorted.sort()
#print("r", r)
#print("r_sorted", r_sorted)
#print("q", q)
for i in range(n):
    lower = bisect_left(r_sorted, r[i])
    ans[i] = max(0, lower - q[i])
print(*ans)
