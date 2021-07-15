#!/usr/bin/env python3
n = int(input())
ts = [input() for i in range(n)]
t = '<3' + '<3'.join(ts) + '<3'
s = input()
i = 0
j = 0
while i < len(t) and j < len(s):
    if t[i] == s[j]:
        i += 1
    j += 1
print(i == len(t) and 'yes' or 'no')

