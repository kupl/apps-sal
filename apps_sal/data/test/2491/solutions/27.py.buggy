from collections import deque
N, M = map(int, input().split())

ABC = []
Adake = [[] for _ in range(N)]
Bdake = [[] for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    ABC.append((a - 1, b - 1, -c))
    Adake[a - 1].append(b - 1)
    Bdake[b - 1].append(a - 1)


def dfs(X, s):
    used = {s}
    search = deque([s])
    while search:
        ss = search.pop()
        for sss in X[ss]:
            if sss in used:
                continue
            used.add(sss)
            search.append(sss)
    return used


U = dfs(Adake, 0) & dfs(Bdake, N - 1)
ABC = [(a, b, c) for (a, b, c) in ABC if a in U and b in U]

INF = float('inf')
dist = [INF] * N
dist[0] = 0
for i in range(N):
    for a, b, c in ABC:
        if dist[b] > dist[a] + c:
            dist[b] = dist[a] + c
            if i == N - 1 and b == N - 1:
                print('inf')
                return
print(-dist[-1])
