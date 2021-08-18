from collections import deque

N, M = map(int, input().split())

edges = [[] for _ in range(N)]

for _ in range(M):
    fr, to = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].append(to)

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

    print(0)
    print()
    return

    loopStart = L[-1]
    while L[0] != loopStart:
        L.popleft()

    print(len(L) - 1)
    ans = [v + 1 for v in L]
    print(*ans[: -1], sep='\n')
    return

print(-1)
