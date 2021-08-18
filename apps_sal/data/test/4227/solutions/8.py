import itertools

N, M = list(map(int, input().split()))

graph = [[False] * N for _ in range(N)]

for _ in range(M):
    a, b = [int(x) - 1 for x in input().split()]
    graph[a][b] = True
    graph[b][a] = True

ans = 0

for path in itertools.permutations(list(range(N)), N):
    if path[0] == 0:
        for i in range(N):
            if i == N - 1:
                ans += 1
                break
            if not graph[path[i]][path[i + 1]]:
                break
print(ans)
