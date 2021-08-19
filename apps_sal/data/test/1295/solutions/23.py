#!/usr/bin/env	python
# -*-coding:utf-8 -*-
n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
B = tuple(map(int, input().split()))
s = i = 0
for c in A:
    while m > i and c > B[i]:
        i += 1
    n = c - B[i - 1]if i else 0x7fffffff
    if m > i:
        n = min(n, B[i] - c)
    s = max(s, n)
print(s)
