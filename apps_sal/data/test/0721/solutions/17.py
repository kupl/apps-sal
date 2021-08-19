#!/usr/bin/env python3

n, d = (int(x) for x in input().split(None, 2))
a = [int(x) for x in input().split()]
assert len(a) == n
m = int(input())

if n <= m:
    print(sum(a) - d * (m - n))
else:
    a.sort()
    print(sum(a[:m]))
