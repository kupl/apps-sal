from collections import deque
(N, M) = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(M)]
es = [[] for _ in range(N)]
for (a, b) in AB:
    (a, b) = (a - 1, b - 1)
    es[a].append(b)
mindist = N
ans = None
for g in range(N):
    for s in es[g]:
        q = deque([s])
        dist = [N] * N
        dist[s] = 0
        prev = [-1] * N
        while q:
            v = q.popleft()
            if v == g:
                break
            for to in es[v]:
                if dist[to] <= dist[v] + 1:
                    continue
                dist[to] = dist[v] + 1
                prev[to] = v
                q.append(to)
        else:
            continue
        if dist[g] >= mindist:
            continue
        mindist = dist[g]
        v = g
        tmp = [v + 1]
        while prev[v] >= 0:
            v = prev[v]
            tmp.append(v + 1)
        ans = tmp
if ans:
    print(len(ans))
    print(*ans, sep='\n')
else:
    print(-1)
