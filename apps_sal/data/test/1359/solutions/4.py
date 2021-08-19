from math import ceil, sqrt, factorial, gcd
from bisect import bisect_left
from collections import deque
from sys import stdin


def input():
    return stdin.readline().strip()


(n, m) = map(int, input().split())
graph = {i: set() for i in range(1, n + 1)}
for i in range(m):
    (a, b) = map(int, input().split())
    graph[a].add(b)
count = 0
for i in range(1, n + 1):
    d = {}
    for j in graph[i]:
        for k in graph[j]:
            if k != i:
                if k in d:
                    d[k] += 1
                else:
                    d[k] = 1
    for k in d:
        count += d[k] * (d[k] - 1) // 2
print(count)
