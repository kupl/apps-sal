from collections import deque
(N, M) = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    (a, b, c) = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
seen = [False] * (N + 1)
count = 0
for i in range(1, N + 1):
    if seen[i] == False:
        seen[i] = True
        S = deque([i])
        while S:
            v = S.popleft()
            for i in graph[v]:
                if seen[i] == False:
                    seen[i] = True
                    S.append(i)
        count += 1
print(count)
