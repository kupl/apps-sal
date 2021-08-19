from math import ceil, sqrt, factorial, gcd
from collections import deque
from sys import stdin


def input():
    return stdin.readline().strip()


(n, m) = map(int, input().split())
l = list(map(int, input().split()))
l = [0] + l
a = [0 for i in range(n + 1)]
a[-1] = n
b = list(a)
for i in range(n - 1, 0, -1):
    if l[i] <= l[i + 1]:
        a[i] = a[i + 1]
    else:
        a[i] = i
    if l[i] >= l[i + 1]:
        b[i] = b[i + 1]
    else:
        b[i] = i
for i in range(m):
    (x, y) = map(int, input().split())
    if b[a[x]] >= y:
        print('Yes')
    else:
        print('No')
