N, M = map(int, input().split())
to = [[] for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    to[a - 1].append(b - 1)
    to[b - 1].append(a - 1)

ans = 0
v = [0] * N


def DFS(n):
    nonlocal ans
    v[n] = 1
    # print(v)
    if sum(v) == N:
        ans += 1
    for i in to[n]:
        if v[i] == 0:
            DFS(i)
    v[n] = 0


DFS(0)
print(ans)
