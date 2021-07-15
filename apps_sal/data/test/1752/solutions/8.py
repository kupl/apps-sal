import math
from collections import deque, defaultdict
from sys import stdin, stdout
input = stdin.readline
listin = lambda : list(map(int, input().split()))
mapin = lambda: map(int, input().split())
n = int(input())
z = listin()
a = deque([])
z.sort()
for i in range(n//2+1):
    if z:
        if i > 0:
            a.append(z[-1])
            z.pop()
        if z:
            a.appendleft(z[-1])
            z.pop()
print(*a)
