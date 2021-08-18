from collections import deque

N, M = map(int, input().split())

edges = [[] for _ in range(N)]
edgesR = [[] for _ in range(N)]

for _ in range(M):
    fr, to = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].append(to)
    edgesR[to].append(fr)

for start in range(N):
    st = deque([(start, True)])
    L = deque()
    V = set()

    while st:
        now, isFirst = st.pop()
        if isFirst:
            L.append(now)

            if now in V:
                break

            V.add(now)

            st.append((now, False))

            for to in edges[now]:
                st.append((to, True))
        else:
            L.pop()
            V.remove(now)
    else:
        continue

    loopStart = L.pop()
    while L[0] != loopStart:
        L.popleft()
    V = set(L)
    dist = [float('inf')] * N
    que = deque([(loopStart, 0)])

    while que:
        now, d = que.popleft()

        if dist[now] <= d:
            if now == loopStart:
                dist[loopStart] = d
                break
            continue
        dist[now] = d

        for to in edges[now]:
            if to in V:
                que.append((to, d + 1))

    ans = [loopStart]
    now = loopStart
    while dist[now] > 1:
        for back in edgesR[now]:
            if dist[now] - 1 == dist[back]:
                ans.append(back)
                now = back
                break

    ans = set([a + 1 for a in ans])
    print(len(ans))
    print(*ans, sep='\n')
    return

print(-1)
