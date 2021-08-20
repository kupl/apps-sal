import sys
import heapq
import math
import fractions
import bisect
import itertools
from collections import Counter
from collections import deque
from operator import itemgetter


def input():
    return sys.stdin.readline().strip()


def mp():
    return list(map(int, input().split()))


def lmp():
    return list(map(int, input().split()))


n = int(input())
edge = [[] for i in range(n + 1)]
par = [0] * (n + 1)
par[1] = -1
col = [0] * (n - 1)
for i in range(n - 1):
    (a, b) = mp()
    edge[a].append([a, b, i])
    edge[b].append([b, a, i])
que = deque([edge[1]])
while len(que):
    k = 1
    q = que.popleft()
    for (x, y, i) in q:
        if col[i] == 0:
            if k == par[x]:
                k += 1
            col[i] = k
            par[y] = k
            k += 1
            que.append(edge[y])
print(max(col))
for i in range(n - 1):
    print(col[i])
