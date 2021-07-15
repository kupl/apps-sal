#!/usr/bin/env python3

n, d = tuple(map(int, input().split(None, 2)))
a = list(map(int, input().split()))
assert len(a) == n
m = int(input())

a.sort()
if n <= m:
    print(sum(a) - d * (m - n))
else:
    print(sum(a[:m]))

