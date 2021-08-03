#!/usr/bin/env python
n, M = list(map(int, input().split()))
t = list(map(int, input().split()))
f = [0 for _ in range(101)]
a = []
for i in range(n):
    Mi = M - t[i]
    c = 0
    for j in range(1, 101):
        k = min(Mi // j, f[j])
        Mi -= k * j
        c += k
    a.append(i - c)
    f[t[i]] += 1
print(' '.join(map(str, a)))
