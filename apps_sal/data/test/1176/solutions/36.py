#!/usr/bin/env python3
n, *a = list(map(int, open(0).read().split()))
for i in range(n - 1):
    if a[i] < 0:
        a[i] *= -1
        a[i + 1] *= -1
print((sum(a) - 2 * min(abs(i) for i in a) - 2 * a[-1] if a[-1] < 0 else sum(a)))
