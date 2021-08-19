import sys
import queue
n = int(input())
clis = [[] for i in range(n)]
for i in range(n - 1):
    (ai, bi, ci) = map(int, input().split())
    clis[ai - 1].append([bi, ci])
    clis[bi - 1].append([ai, ci])
(q, k) = map(int, input().split())
xy = []
for i in range(q):
    xy.append(list(map(int, input().split())))
distance = [0 for i in range(n)]
seen = [0 for i in range(n)]
que = queue.Queue()
que.put(k)
seen[k - 1] = 1
while not que.empty():
    c = que.get()
    for (aa, cc) in clis[c - 1]:
        if seen[aa - 1] == 0:
            distance[aa - 1] = distance[c - 1] + cc
            seen[aa - 1] = 1
            que.put(aa)
for i in range(q):
    print(distance[xy[i][0] - 1] + distance[xy[i][1] - 1])
