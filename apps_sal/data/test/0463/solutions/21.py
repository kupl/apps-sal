#!/usr/bin/env python3
from sys import stdin, stdout

def rint():
    return map(int, stdin.readline().split())
#lines = stdin.readlines()


n, x = rint()

a = list(rint())

a_dict = dict()
for i in range(n):
    if a[i] not in a_dict:
        a_dict[a[i]] = 1
    else:
        a_dict[a[i]] += 1

if n > len(a_dict):
    print("0")
    return

for i in range(n):
    if a[i]&x in a_dict:
        if a[i]&x == a[i]:
            if a_dict[a[i]&x] >= 2:
                print("1")
                return
        else:
            print("1")
            return

ax = [a[i]&x for i in range(n)]

ax_set = set(ax)

if n > len(ax_set):
    print("2")
else:
    print("-1")
