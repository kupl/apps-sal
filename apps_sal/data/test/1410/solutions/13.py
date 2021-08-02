#!/usr/bin/env python3
import sys
from itertools import permutations
from math import inf

#lines = stdin.readlines()


def rint():
    return list(map(int, sys.stdin.readline().split()))


def input():
    return sys.stdin.readline().rstrip('\n')


def oint():
    return int(input())


n = oint()

c = []
for i in range(3):
    c.append(list(rint()))

adj = [set() for i in range(n)]
for i in range(n - 1):
    u, v = rint()
    u -= 1
    v -= 1
    adj[u].add(v)
    adj[v].add(u)
for i in range(n):
    if len(adj[i]) >= 3:
        print(-1)
        return
    if len(adj[i]) == 1:
        start = i
minv = inf
i = [0] * 3
ord = []
cur = start
v = [0] * n
v[cur] = 1
for j in range(n):
    ord.append(cur)
    for next in adj[cur]:
        if v[next] == 0:
            v[next] = 1
            cur = next
            break

for i[0], i[1], i[2] in permutations([0, 1, 2]):
    v = 0
    for j in range(n):
        v += c[i[j % 3]][ord[j]]
    if v < minv:
        imin = i.copy()
        minv = v
ans = [0] * n
for j in range(n):
    ans[ord[j]] = imin[j % 3] + 1
print(minv)
print(*ans)
