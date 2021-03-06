import copy
import random
import bisect
import fractions
import math
import sys
import collections
from decimal import Decimal
mod = 10 ** 9 + 7
sys.setrecursionlimit(mod)
d = collections.deque()


def LI():
    return list(map(int, sys.stdin.readline().split()))


N = int(input())
weights = {}
roots = [[] for i in range(N)]
for i in range(N - 1):
    (a, b, c) = LI()
    a -= 1
    b -= 1
    roots[a].append(b)
    roots[b].append(a)
    weights[a, b] = c
    weights[b, a] = c
(Q, K) = LI()
K -= 1
xy = [0 for i in range(Q)]
for i in range(Q):
    (x, y) = LI()
    x -= 1
    y -= 1
    xy[i] = [x, y]
'\nxyzで全部の通りを見つけるとN ** 3で無理\nなので今回は木構造に注目してBFS or DFSで解いたらいいのでは？\n重みを単純にグラフに持つと10**5 ** 2になってしまうので注意\n'
visited = [-1 for i in range(N)]
queue = collections.deque()
queue.append(K)
visited[K] = 0
while len(queue) > 0:
    node = queue.popleft()
    cnt = visited[node]
    for n_node in roots[node]:
        if visited[n_node] == -1:
            visited[n_node] = cnt + weights[node, n_node]
            queue.append(n_node)
for (x, y) in xy:
    print(visited[x] + visited[y])
