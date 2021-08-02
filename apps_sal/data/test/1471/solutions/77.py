def inpl(): return list(map(int, input().split()))


N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = inpl()
    G[u - 1].append((v - 1, w))
    G[v - 1].append((u - 1, w))

Q = [(0, 0)]
searched = [0] * N
searched[0] = 1
ans = [-1] * N
ans[0] = 0

while Q:
    p, c = Q.pop()
    for q, d in G[p]:
        if searched[q]:
            continue
        ans[q] = (c + d) % 2
        searched[q] = 1
        Q.append((q, ans[q]))
print(*ans, sep="\n")
