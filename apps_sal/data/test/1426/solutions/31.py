from collections import defaultdict, deque


def kenkenpa(s, visited):
    res = []
    for v1 in e[s]:
        if visited[v1][1]:
            continue
        visited[v1][1] = True
        for v2 in e[v1]:
            if visited[v2][2]:
                continue
            visited[v2][2] = True
            for v3 in e[v2]:
                if visited[v3][0]:
                    continue
                visited[v3][0] = True
                res.append(v3)
    return res


(N, M) = list(map(int, input().split()))
e = defaultdict(list)
for i in range(M):
    (u, v) = list(map(int, input().split()))
    e[u].append(v)
(S, T) = list(map(int, input().split()))
q = deque([[S, 0]])
visited = [[False] * 3 for _ in range(N + 1)]
visited[S][0] = True
ans = -1
while q:
    (u, c) = q.popleft()
    if u == T:
        ans = c
        break
    l = kenkenpa(u, visited)
    for v in l:
        q.append([v, c + 1])
print(ans)
