#!/usr/bin/env python3
from sys import stdin, stdout


def rint():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()


a, b = rint()

for i in range(1, 10**9):
    if i % 2:
        a -= i
    else:
        b -= i

    if a < 0:
        print("Vladik")
        return
    if b < 0:
        print("Valera")
        return
