import sys
import heapq as hq
import itertools
import math
import collections


def ma():
    return map(int, input().split())


def lma():
    return list(map(int, input().split()))


def tma():
    return tuple(map(int, input().split()))


def ni():
    return int(input())


def yn(fl):
    return print('YES') if fl else print('NO')


def ips():
    return input().split()


n = ni()
A = lma()
mx = 0
ans = []
pal = 1
idx = 0
for i in range(n):
    if mx < abs(A[i]):
        mx = abs(A[i])
        pal = A[i] // mx
        idx = i
if pal == 1:
    for i in range(n):
        if i == idx:
            continue
        ans.append((idx + 1, i + 1))
    for i in range(n - 1):
        ans.append((i + 1, i + 2))
else:
    for i in range(n):
        if i == idx:
            continue
        ans.append((idx + 1, i + 1))
    for i in range(n - 1, 0, -1):
        ans.append((i + 1, i))
print(len(ans))
for (x, y) in ans:
    print(x, y)
