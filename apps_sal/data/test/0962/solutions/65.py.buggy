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

    loopStart = L.pop()
    while L[0] != loopStart:
        L.popleft()

    ans = []
    K = len(L)
    for i, now in enumerate(L):
        for to in edges[now]:
            if i + 1 >= K or to == L[i + 1]:
                ans.append(now + 1)
                break
        else:
            break
    else:
        print(0)
        print()
        # print(len(ans))
        # print(*ans, sep='\n')
        return

print(-1)
