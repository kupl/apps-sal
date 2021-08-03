N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]
shift = 10**5 + 1

nodes = {}
visited = {}

for x, y in xy:
    y += shift
    if x in nodes:
        nodes[x].append(y)
    else:
        nodes[x] = [y]
    if y in nodes:
        nodes[y].append(x)
    else:
        nodes[y] = [x]
    visited[x] = False
    visited[y] = False

ans = 0


def dfs(s, nodes, visited):
    q = [s]
    cnt_x = 0
    cnt_y = 0

    while q:
        v = q.pop()
        if visited[v]:
            continue
        visited[v] = True

        if v // shift < 1:
            cnt_x += 1
        else:
            cnt_y += 1

        q.extend(nodes[v])

    return visited, cnt_x * cnt_y


for s in nodes:
    if visited[s]:
        continue
    visited, cnt = dfs(s, nodes, visited)
    ans += cnt

print(ans - N)
