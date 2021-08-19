from collections import deque
(N, M) = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    (A, B) = map(int, input().split())
    edge[A - 1].append(B - 1)
ans = []
for sta in range(N):
    prev = [-1] * N
    que = deque([sta])
    while que:
        v = que.popleft()
        for w in edge[v]:
            if w == sta:
                path = []
                while v != -1:
                    path.append(v + 1)
                    v = prev[v]
                if not ans or len(ans) > len(path):
                    ans = path
                break
            if prev[w] != -1:
                continue
            prev[w] = v
            que.append(w)
if ans:
    print(len(ans))
    print(*ans, sep='\n')
else:
    print(-1)
