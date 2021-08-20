from collections import deque
(N, K) = map(int, input().split())
mod = 10 ** 9 + 7
G = [[] for _ in range(N)]
for i in range(N - 1):
    (a, b) = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


def bfs(s):
    seen = [0] * N
    prev = [0] * N
    color = [0] * N
    todo = deque()
    seen[s] = 1
    todo.append(s)
    color[s] = K
    while todo:
        a = todo.popleft()
        if a == start:
            count = K - 1
        else:
            count = K - 2
        for b in G[a]:
            if seen[b] == 0:
                seen[b] = 1
                todo.append(b)
                prev[b] = a
                color[b] = count % mod
                count -= 1
    return color


(MAX, start) = (0, -1)
for i in range(N):
    if len(G[i]) > MAX:
        MAX = len(G[i])
        start = i
color = bfs(start)
ans = 1
for i in range(N):
    ans *= color[i]
    ans %= mod
print(ans)
