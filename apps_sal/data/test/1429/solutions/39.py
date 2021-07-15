import sys
from collections import *
input = sys.stdin.readline

n, s = input().split()
x = y = r = 0
d = Counter()
for c in s:
    d[x,y] += 1
    if c == 'A':
        x += 1
    elif c == 'T':
        x -= 1
    elif c == 'C':
        y += 1
    elif c == 'G':
        y -= 1
    r += d[x,y]
    
print(r)

