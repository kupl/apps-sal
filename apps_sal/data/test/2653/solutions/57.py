import collections
import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))


N, Q = LI()
ab = [LI() for _ in range(N - 1)]
px = [LI() for _ in range(Q)]
ans = [0] * (N + 1)
graph = {i: collections.deque() for i in range(1, N + 1)}
for a, b in ab:
    graph[a].append(b)
    graph[b].append(a)
for p, x in px:
    ans[p] += x
seen = [0] * (N + 1)
stack = []


def dfs():
    seen[1] = 1
    stack.append(1)
    while stack:
        s = stack.pop()
        if not graph[s]:
            continue
        for j in range(len(graph[s])):
            g_NO = graph[s].popleft()
            if seen[g_NO]:
                continue
            seen[g_NO] = 1
            stack.append(g_NO)
            ans[g_NO] += ans[s]


dfs()
print(*ans[1:])
