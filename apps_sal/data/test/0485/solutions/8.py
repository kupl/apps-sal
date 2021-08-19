from collections import deque, defaultdict
import math
import sys
import string
import bisect
import heapq
input = sys.stdin.readline


def L():
    return list(map(int, input().split()))


def Ls():
    return list(input().split())


def M():
    return list(map(int, input().split()))


def I():
    return int(input())


n = I()
l = []
x = defaultdict(int)
y = defaultdict(int)
for i in range(4 * n + 1):
    a = L()
    l.append(a)
    x[a[0]] += 1
    y[a[1]] += 1
l.sort()
leftx = l[0][0]
if x[l[0][0]] == 1 or x[l[0][0]] > n + 2:
    keyx = l[0][0]
    leftx = l[1][0]
rightx = l[-1][0]
if x[l[-1][0]] == 1 or x[l[-1][0]] > n + 2:
    keyx = l[-1][0]
    rightx = l[-2][0]
l.sort(key=lambda x: x[1])
downy = l[0][1]
if y[l[0][1]] == 1 or y[l[0][1]] > n + 2:
    keyy = l[0][1]
    downy = l[1][1]
upy = l[-1][1]
if y[l[-1][1]] == 1 or y[l[-1][1]] > n + 2:
    upy = l[-2][1]
    keyy = l[-1][1]
c = 0
for i in l:
    if i[0] == leftx:
        if i[1] <= upy and i[1] >= downy:
            c += 1
        else:
            print(*i)
            break
    elif i[0] == rightx:
        if i[1] <= upy and i[1] >= downy:
            c += 1
        else:
            print(*i)
            break
    elif i[1] == downy:
        if i[0] >= leftx and i[0] <= rightx:
            c += 1
        else:
            print(*i)
            break
    elif i[1] == upy:
        if i[0] >= leftx and i[0] <= rightx:
            c += 1
        else:
            print(*i)
            break
    else:
        print(*i)
        break
