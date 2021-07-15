#!/usr/bin/env python3
from sys import stdin,stdout


def ri():
    return list(map(int, input().split()))


s = input()
l = len(s)
v = [0 for i in range(l)]

if l == 1:
    print(0)
    return


count = 0
for i in range(l-1):
    if v[i]:
        continue
    if s[i:i+2] == "VK":
        v[i] = 1
        v[i+1] = 1
        count += 1

for i in range(l-1):
    if v[i] or v[i+1]:
        continue

    if s[i:i+2] == "VV" or s[i:i+2] == "KK":
        count += 1
        break

print(count)


