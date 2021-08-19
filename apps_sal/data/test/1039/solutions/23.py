from collections import deque
N = int(input())
G = [{} for _ in range(N + 1)]
for i in range(N - 1):
    (a, b, c) = map(int, input().split())
    G[a][b] = G[b][a] = c


def bfs(s):
    seen = [0 for i in range(N + 1)]
    d = [0 for i in range(N + 1)]
    cross = []
    todo = deque()
    seen[s] = 1
    todo.append(s)
    while 1:
        if len(todo) == 0:
            break
        a = todo.popleft()
        for b in G[a].keys():
            if seen[b] == 0:
                seen[b] = 1
                todo.append(b)
                d[b] += d[a] + G[a][b]
    return d


(Q, K) = map(int, input().split())
d = bfs(K)
for q in range(Q):
    (x, y) = map(int, input().split())
    print(d[x] + d[y])
