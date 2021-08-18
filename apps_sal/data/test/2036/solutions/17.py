import math
from collections import deque
from sys import stdin, stdout
from string import ascii_letters
input = stdin.readline
letters = ascii_letters[:26]

n, m, x, y = list(map(int, input().split()))
print(x, y)
for i in range(x, n + 1):
    if i % 2:
        for g in range(1, m + 1):
            if (i, g) == (x, y):
                continue
            print(i, g)
    else:
        for g in range(m, 0, -1):
            if (i, g) == (x, y):
                continue
            print(i, g)
inv = n % 2
for i in range(1, x):
    if (i % 2) if not inv else (1 - (i % 2)):
        for g in range(1, m + 1):
            if (i, g) == (x, y):
                continue
            print(i, g)
    else:
        for g in range(m, 0, -1):
            if (i, g) == (x, y):
                continue
            print(i, g)
