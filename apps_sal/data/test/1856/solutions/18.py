#!/usr/bin/env python3
import sys

#lines = stdin.readlines()


def rint():
    return list(map(int, sys.stdin.readline().split()))


def input():
    return sys.stdin.readline().rstrip('\n')


def oint():
    return int(input())


n = oint()

node = dict()
for _ in range(n):
    s = set(input())
    for c1 in s:
        if not c1 in node:
            node[c1] = s
        else:
            node[c1] = node[c1].union(s)
v = set()


def dfs(k):
    if k in v:
        return
    v.add(k)
    for kk in node[k]:
        if not kk in v:
            dfs(kk)
    return


ans = 0
for k in node:
    if k in v:
        continue
    ans += 1
    dfs(k)

print(ans)
