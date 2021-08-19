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
a = []
m = dict()
for i in range(n - 2):
    q = list(rint())
    a.append(q)
    for j in range(3):
        if q[j] in m:
            m[q[j]] = m[q[j]] + [i]

        else:
            m[q[j]] = [i]
start = []
second = []
for j in range(1, n + 1):
    if len(m[j]) == 1:
        start.append(j)
    if len(m[j]) == 2:
        second.append(j)
s = start[0]
if m[s][0] in m[second[0]]:
    sec = second[0]
else:
    sec = second[1]
ans = [s, sec]
for i in range(2, n):
    qi = set(m[ans[i - 2]]).intersection(set(m[ans[i - 1]]))
    if len(qi) == 1:
        next = set(a[qi.pop()]).difference(set([ans[i - 2], ans[i - 1]])).pop()
    else:
        next1 = set(a[qi.pop()]).difference(set([ans[i - 2], ans[i - 1]])).pop()
        next2 = set(a[qi.pop()]).difference(set([ans[i - 2], ans[i - 1]])).pop()
        if next1 == ans[-3]:
            next = next2
        else:
            next = next1
    ans.append(next)


print(*ans)
