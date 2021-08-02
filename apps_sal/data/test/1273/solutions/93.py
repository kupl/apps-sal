from collections import deque
N = int(input())
E = [[] for _ in range(N)]

for i in range(N - 1):
    a, b = list(map(int, input().split()))
    a, b = a - 1, b - 1
    # 出力のために、何番目のEdgeだったかを保有させる必要がある
    E[a].append([i, b])
    E[b].append([i, a])

k = 0
for e in E:
    k = max(k, len(e))
print(k)


def bfs():
    colors = [-1 for _ in range(N - 1)]
    visited = [False for _ in range(N)]
    d = deque()
    d.append([0, -1])
    while d:
        now, edge_color = d.pop()
        visited[now] = True
        cand_color = 1
        for i, nxt in E[now]:
            #print(i, nxt, visited[i], colors[i])
            if visited[nxt]:
                continue  # TreeでBFSだとここは通らない・・・？
            if colors[i] > -1:
                assert("１エッジに２色塗ろうとする・・・？")
                continue
            if cand_color == edge_color:
                cand_color += 1
            colors[i] = cand_color
            d.append([nxt, colors[i]])
            cand_color += 1
    return colors


colors = bfs()

for i in range(len(colors)):
    print(colors[i])
