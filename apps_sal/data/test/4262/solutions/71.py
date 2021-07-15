# -*- coding: utf-8 -*-
import itertools

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

a = 0
b = 0
for i, r in enumerate(itertools.permutations(list(range(1, n+1)))):
    if r == p:
        a = i
    if r == q:
        b = i

print((abs(a - b)))

