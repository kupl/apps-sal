N = int(input())
G = [[] for n in range(N + 1)]
q = [(1, 0)]
ans = N * [-1]

for n in range(N - 1):
    u, v, w = map(int, input().split())
    G[u] += [(v, w)]
    G[v] += [(u, w)]

while q:
    x, y = q.pop()
    ans[x - 1] = y % 2
    for g, d in G[x]:
        q += [(g, y + d)] * (ans[g - 1] < 0)

print(*ans, sep="\n")
