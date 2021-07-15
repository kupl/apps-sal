from collections import deque
import sys

input = sys.stdin.buffer.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
infi = 10 ** 10


def bfs(start):
    # res = 頂点数, サイクル最後の頂点、で持つ
    res = (infi, -1)
    dist = [-1] * (n + 1)
    par = [-1] * (n + 1)
    que = deque([])
    que.append(start)
    dist[start] = 0
    while que:
        v = que.popleft()
        for u in graph[v]:
            if dist[u] >= 0:
                continue
            dist[u] = dist[v] + 1
            par[u] = v
            que.append(u)
    for i in range(1, n + 1):
        if i == start:
            continue
        if dist[i] == -1:
            continue
        if start in graph[i]:
            if res[0] > dist[i] + 1:
                res = (dist[i] + 1, i)
    if res[0] == infi:
        return -1, []
    cycle_num = res[0]
    v = res[1]
    CYCLE = deque([])
    while v > 0:
        CYCLE.appendleft(v)
        v = par[v]

    return cycle_num, CYCLE


jisho = {}
ans = (-1, [])
cycle_num = infi
kouho_v = -1
for i in range(1, n + 1):
    temp_num, temp_cycle = bfs(i)
    if temp_num == -1:
        continue
    if cycle_num > temp_num:
        cycle_num = min(cycle_num, temp_num)
        kouho_v = i
        jisho[i] = temp_cycle

if kouho_v == -1:
    print(-1)
    return
else:
    ans_num = cycle_num
    ans_list = jisho[kouho_v]
    print(cycle_num)
    print(*ans_list, sep="\n")

