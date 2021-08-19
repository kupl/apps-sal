from collections import deque
import sys
import math
import string
input = sys.stdin.readline


def L():
    return list(map(int, input().split()))


def Ls():
    return list(input().split())


def M():
    return list(map(int, input().split()))


n = int(input())
l = L()
l.sort()
g = deque([])
for i in range(n):
    if i % 2 == 0:
        g.append(l[i])
    else:
        g.appendleft(l[i])
print(*g)
