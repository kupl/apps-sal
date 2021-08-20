import sys
from collections import deque, defaultdict
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N = int(readline())
graph = [[] for _ in range(N + 1)]
AB = []
for i in range(N - 1):
    (a, b) = map(int, readline().split())
    AB.append((a, b))
    graph[a].append(b)
    graph[b].append(a)
dist = [-1] * (N + 1)
dist[1] = 0
COL = defaultdict()
q = deque([(1, 0)])
max_col = 0


def bfs(max_col):
    while q:
        (x, pre_col) = q.popleft()
        c = 1
        for nx in graph[x]:
            if dist[nx] != -1:
                continue
            if c == pre_col:
                c += 1
            COL[x, nx] = c
            dist[nx] = 1
            q.append((nx, c))
            max_col = max(max_col, c)
            c += 1
    return max_col


max_col = bfs(max_col)
print(max_col)
for (a, b) in AB:
    if (a, b) in COL:
        print(COL[a, b])
    else:
        print(COL[b, a])
