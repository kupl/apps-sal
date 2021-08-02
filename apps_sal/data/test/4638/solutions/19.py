#!/usr/bin/env python3
import sys
from math import inf

#lines = stdin.readlines()


def rint():
    return list(map(int, sys.stdin.readline().split()))


def input():
    return sys.stdin.readline().rstrip('\n')


def oint():
    return int(input())


n, c = rint()

a = list(rint())
b = list(rint())

e = 0
ans = [0]
e = [0] * (n + 2)
mina = [inf] * (n + 2)
mine = [inf] * (n + 2)
mina[0] = a[0]
mine[0] = b[0] + c
for i in range(1, n - 1):
    mine[i] = b[i] + min(mine[i - 1], mina[i - 1] + c, mine[i - 2] + mine[i - 1])
    mina[i] = a[i] + min(mina[i - 1], mine[i - 1])

for i in range(n - 1):
    ans.append(min(mine[i], mina[i]))

print(*ans)
