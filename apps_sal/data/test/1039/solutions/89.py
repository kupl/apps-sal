from collections import deque
N = int(input())
t = [[] for _ in range(N)]
for _ in range(N - 1):
    (a, b, c) = list(map(int, input().split()))
    t[a - 1].append([b, c])
    t[b - 1].append([a, c])
(Q, K) = list(map(int, input().split()))
visited = [-1 for _ in range(N)]
visited[K - 1] = 0
que = deque()
que.append(K)
while len(que):
    now = que.popleft()
    for (nxt, c) in t[now - 1]:
        if visited[nxt - 1] != -1:
            continue
        visited[nxt - 1] = visited[now - 1] + c
        que.append(nxt)
for i in range(Q):
    (x, y) = list(map(int, input().split()))
    print(visited[x - 1] + visited[y - 1])
