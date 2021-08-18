#!/usr/bin/env python3
from sys import stdin, stdout


def rint():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()


def check(i, j):
    for r in range(n):
        for c in range(n):
            if a[i][c] + a[r][j] == a[i][j]:
                return 1
    return 0


n = int(input())
a = [[] for _ in range(n)]
for i in range(n):
    a[i] = list(rint())

for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            continue
        if check(i, j) == 0:
            print("No")
            return

print("Yes")
