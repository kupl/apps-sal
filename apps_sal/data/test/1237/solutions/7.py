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

n, s = list(map(int, input().split()))
time = 0
for f, t in sorted(list(map(int, input().split())) for x in range(n)):
    time = max(time + s - f, t)
    s = f
print(time + s)

