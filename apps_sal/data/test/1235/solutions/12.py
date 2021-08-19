import sys
import re
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from bisect import bisect_left, bisect_right


def dfs(curr, parent):
    visited[curr] = True
    value[curr] += value[parent]
    for i in mydict[curr]:
        if not visited[i]:
            dfs(i, curr)


def get_array():
    return list(map(int, sys.stdin.readline().strip().split()))


def get_ints():
    return map(int, sys.stdin.readline().strip().split())


def input():
    return sys.stdin.readline().strip()


n = int(input())
A = get_array()
A.sort()
m = int(input())
B = get_array()
B.sort()
print(A[-1], B[-1])
