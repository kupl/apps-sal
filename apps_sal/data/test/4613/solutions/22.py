N, M = map(int, input().split())
to1 = [[0] for i in range(N)]
ab = [[0, 0] for i in range(M)]

for i in range(M):
    ab[i][0], ab[i][1] = map(int, input().split())
    to1[ab[i][0] - 1].append(ab[i][1] - 1)
    to1[ab[i][1] - 1].append(ab[i][0] - 1)

ans = 0


def DFS(n):
    nonlocal v
    if v[n] == 1:
        return
    v[n] = 1
    for i in to1[n]:
        DFS(i)


for i in range(M):
    v = [0] * N
    p = ab[i]
    p[0] -= 1
    p[1] -= 1
    to1[p[0]].remove(p[1])
    to1[p[1]].remove(p[0])
    DFS(0)
    if sum(v) != N:
        ans += 1
    to1[p[0]].append(p[1])
    to1[p[1]].append(p[0])

print(ans)
