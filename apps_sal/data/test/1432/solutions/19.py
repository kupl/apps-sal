#!/usr/bin/env python3
n, *a = list(map(int, open(0).read().split()))
b = [0]
for i in a:
    b[0] = i - b[0]
for i in a:
    b.append((i - b[-1] // 2) * 2)
print((*b[:n]))
