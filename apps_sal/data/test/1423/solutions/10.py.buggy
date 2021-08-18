#!/usr/bin/env python3
from sys import stdin, stdout


def ri():
    return list(map(int, input().split()))


n, l, r = ri()
a = list(ri())
p = list(ri())

pi = [i for i in range(n)]
pi.sort(key=lambda e: p[e])
b = [0 for i in range(n)]

i = pi[0]
b[i] = l
cp = b[i] - a[i]
for ii in range(1, n):
    i = pi[ii]
    if a[i] + cp + 1 >= l:
        b[i] = a[i] + cp + 1
    else:
        b[i] = l

    cp = b[i] - a[i]
    if b[i] > r:
        print(-1)
        return

print(*b)
