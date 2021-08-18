#!/usr/bin/env python3
from sys import stdin, stdout


def ri():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()


n, k = ri()

if k > n * n:
    print(-1)
    return

m = [[0 for _ in range(n)] for __ in range(n)]

for i in range(n):
    if k == 1:
        m[i][i] = 1
        k -= 1
        break
    if k == 0:
        break
    m[i][i] = 1
    k -= 1
    for j in range(i + 1, n):
        if k == 1:
            m[i + 1][i + 1] = 1
            k -= 1
            break
        if k == 0:
            break
        m[i][j] = 1
        m[j][i] = 1
        k -= 2

for i in range(n):
    print(*m[i])
