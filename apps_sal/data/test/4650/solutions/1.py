#!/usr/bin/env python
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    f = [0, 0, 0]
    for ai in a:
        f[ai % 3] += 1
    m = min(f[1], f[2])
    f[1] -= m; f[2] -= m
    print(f[0] + m + (f[1] + f[2]) // 3)

