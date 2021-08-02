# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 18:52:59 2019

@author: phamv
"""
# Function Definition


def find(x):
    while f[x] != x:
        f[x] = f[f[x]]
        x = f[x]
    return x


def merge(u, v):
    u, v = map(find, (u, v))
    f[u] = v;
    if u == v:
        return False
    ret = s[u] > 0 and s[v] > 0
    s[v] += s[u]
    return ret

###############


n, m, k = map(int, input().split())
x = list(map(int, input().split()))
lst = list()
for i in range(m):
    lst.append(tuple(map(int, input().split())))
lst.sort(key=lambda x: x[2])

f = list(range(n + 1))
s = [0] * (n + 1)

for j in x:
    s[j] += 1

for h in lst:
    if merge(h[0], h[1]):
        answer = h[2]

print(*[answer] * k)
