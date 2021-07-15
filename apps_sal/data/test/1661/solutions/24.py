#!/usr/bin/env python3
from sys import stdin, stdout

def rint():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()


n, m = rint()

c = list(rint())
a = list(rint())

j = 0
cnt = 0
for i in range(n):
    if j >= m:
        break
    if c[i] <= a[j]:
        cnt += 1
        j += 1

print(cnt)



