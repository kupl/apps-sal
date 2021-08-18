import sys
import queue

n = int(input())
e = [[] for _ in range(n + 1)]
for i in range(n - 1):
    u, v, w = list(map(int, input().split()))
    e[u].append((v, w))
    e[v].append((u, w))


volt = [False for _ in range(n + 1)]
dst = [0 for i in range(n + 1)]

q = queue.Queue()

q.put(0)

while (not q.empty()):
    curr = q.get()
    volt[curr] = True
    for nb in e[curr]:
        if (not volt[nb[0]]):
            dst[nb[0]] = dst[curr] + nb[1]
            q.put(nb[0])
            volt[nb[0]] = True

print(max(dst))
