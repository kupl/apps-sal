
N = int(input())
graph = [[] for _ in range(N)]
color = [-1] * N

for i in range(N - 1):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    w %= 2
    graph[a].append((b, w))
    graph[b].append((a, w))

next_q = [(0, 0)]
while len(next_q) > 0:
    nw, nc = next_q.pop()
    color[nw] = nc
    for nxt, nl in graph[nw]:
        if color[nxt] == -1:
            next_q.append((nxt, (nl + nc) % 2))
for i in color:
    print(i)
