from collections import defaultdict as dd
import math
import heapq


def nn():
    return int(input())


def li():
    return list(input())


def mi():
    return list(map(int, input().split()))


def lm():
    return list(map(int, input().split()))


n = nn()
parentlist = []
for i in range(n):
    parentlist.append(lm())
childlist = dd(list)
for i in range(1, n + 1):
    childlist[i] = []
for (vertex, pair) in enumerate(parentlist):
    parent = pair[0]
    if not parent == -1:
        childlist[parent].append((vertex + 1, pair[1]))
blist = []
for vertex in childlist:
    if childlist[vertex] == [] or all([child[1] == 1 for child in childlist[vertex]]):
        if parentlist[vertex - 1][1] == 1:
            blist.append(vertex)
deleted = sorted(blist)
if len(deleted) == 0:
    print(-1)
else:
    print(*deleted)
