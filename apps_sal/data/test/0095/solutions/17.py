#!/usr/bin/env python3
from sys import stdin, stdout


def rint():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()


n = int(input())
a = list(rint())

if n == 1:
    print("YES")
    return

stage = 0
for i in range(n - 1):
    diff = a[i + 1] - a[i]
    if stage == 0:
        if diff > 0:
            pass
        elif diff == 0:
            stage = 1
        else:
            stage = 2
    elif stage == 1:
        if diff > 0:
            print("NO")
            return
        elif diff == 0:
            pass
        else:
            stage = 2
    elif stage == 2:
        if diff > 0 or diff == 0:
            print("NO")
            return
        else:
            pass
print("YES")
