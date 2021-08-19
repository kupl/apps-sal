#!/usr/bin/env python3
(n, ), *q = [[*map(int, i.split())] for i in open(0)]
ans = [0] * n
for i, p in enumerate(q):
    c, s, f = p
    for j in range(i):
        ans[j] = c + max(s, -(-ans[j] // f) * f)
    ans[i] = c + s
print(*ans, sep="\n")
