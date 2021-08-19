#!/usr/bin/env python
n, M = list(map(int, input().split()))
t = list(map(int, input().split()))
a = []
for i in range(n):
    ti = sorted(t[:i])
    Mi = M - t[i]
    s = 0
    j = 0
    while j < i:
        s += ti[j]
        if s > Mi:
            break
        j += 1
    a.append(i - j)
print(*a)
