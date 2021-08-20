from collections import deque
(N, M) = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(M)]
es = [[] for i in range(N)]
for (a, b) in AB:
    (a, b) = (a - 1, b - 1)
    es[a].append(b)
tmpdist = N
ans = None
for to in range(N):
    for fr in es[to]:
        dist = [N] * N
        dist[fr] = 0
        prev = [-1] * N
        q = deque([fr])
        while q:
            v = q.popleft()
            if v == to:
                break
            for w in es[v]:
                if dist[w] < N:
                    continue
                if v == to and w == fr:
                    continue
                dist[w] = dist[v] + 1
                prev[w] = v
                q.append(w)
        else:
            continue
        if dist[to] < tmpdist:
            tmpdist = dist[to]
            ans = set()
            v = to
            while 1:
                ans.add(v + 1)
                if prev[v] < 0:
                    break
                v = prev[v]
if ans is None:
    print(-1)
else:
    print(len(ans))
    print(*ans, sep='\n')
