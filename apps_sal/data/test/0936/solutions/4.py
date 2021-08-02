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

n = int(input())
ans = -1
d = {-1: -1}
for a in map(int, input().split()):
    d[a] = d.get(a, 0) + 1
    if d[a] > d[ans]:
        ans = a
print(ans)
