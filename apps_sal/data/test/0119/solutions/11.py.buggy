#!/usr/bin/env python3
from sys import stdin, stdout


def rint():
    return list(map(int, stdin.readline().split()))


n = int(input())

a = [list(rint()) + [i + 1] for i in range(n)]

a.sort(key=lambda aa: [aa[0], -aa[1], aa[2]])

start = [-1, -1, -1]

for aa in a:
    if start[1] >= aa[1]:
        ans = [aa[2], start[2]]
        print(*ans)
        return
    else:
        start = aa

print(-1, -1)
