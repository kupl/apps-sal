import math
import sys
from sys import stdin, stdout
from collections import Counter, defaultdict, deque
input = stdin.readline
def I(): return int(input())
def li(): return list(map(int, input().split()))


def case():
    n, q = li()
    a = li()
    up = [0] * n
    down = [0] * n
    i = 0
    while(i < n):
        j = i
        while(j < n - 1 and a[j] <= a[j + 1]):
            j += 1
        for k in range(i, j + 1):
            up[k] = j
        i = j + 1
    i = 0
    while(i < n):
        j = i
        while(j < n - 1 and a[j] >= a[j + 1]):
            j += 1
        for k in range(i, j + 1):
            down[k] = j
        i = j + 1
    for i in range(q):
        l, r = li()
        p = up[l - 1]
        q = down[p]
        if(q + 1 >= r):
            print("Yes")
        else:
            print("No")


for _ in range(1):
    case()
