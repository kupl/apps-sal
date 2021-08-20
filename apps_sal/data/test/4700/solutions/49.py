(N, M) = map(int, input().split())
H = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for query in range(M):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
ans = 0
for now in range(N):
    good = True
    for neighbor in graph[now]:
        if H[now] <= H[neighbor]:
            good = False
    if good:
        ans += 1
print(ans)
