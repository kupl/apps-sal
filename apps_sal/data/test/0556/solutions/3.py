#!/bin/python
import collections
import random
import sys
try:
    from tqdm import tqdm
except:
    def tqdm(iterable):
        return iterable


__taskname = ''
if __taskname:
    sys.stdin = open(__taskname + '.in')
    sys.stdout = open(__taskname + '.out', 'w')

l, r, k = list(map(int, input().split()))
a, x, i = [], 1, 0
while x <= r:
    if x >= l:
        a.append(x)
    x *= k
    i += 1
print(*(a if a else [-1]))
