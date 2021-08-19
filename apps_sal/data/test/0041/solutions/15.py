#!/usr/bin/env python3
from sys import stdin, stdout


def ri():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()


n = int(input())
a = list(ri())

for i in range(n):
    if a[i] != 0:
        a[i] = -1

for i in range(n):
    if a[i] != 0:
        continue
    for j in range(i + 1, n):
        if a[j] == 0:
            break
        if a[j] == -1 or a[j] > j - i:
            a[j] = j - i
    for j in range(i - 1, -1, -1):
        if a[j] == 0:
            break
        if a[j] == -1 or a[j] > i - j:
            a[j] = i - j

print(" ".join(map(str, a)))
