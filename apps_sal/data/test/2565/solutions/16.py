from math import ceil
from sys import stdin, stdout, setrecursionlimit
from random import randint
for _ in range(int(input())):
    (x1, y1, z1) = list(map(int, input().split()))
    (x2, y2, z2) = list(map(int, input().split()))
    x = min(z1, y2)
    z1 -= x
    y2 -= x
    ans = x * 2
    z2 = max(0, z2 - z1 - x1)
    print(ans - min(z2, y1) * 2)
