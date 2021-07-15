import sys
sys.setrecursionlimit(10000000)
N = int(input())
ab = [list(map(int, input().split())) for _ in range(N-1)]

path = [list() for _ in range(N+1)]
for i in range(N-1):
    a, b = ab[i][0], ab[i][1]
    path[a].append([b, i])
    path[b].append([a, i])

color_max = 0
color_list = [0]*(N-1)
visit = [False]*(N+1)
visit[1] = True
def dfs(node, color, used_path):
    nonlocal visit
    nxt_color = 0
    for nxt in path[node]:
        nxt_node = nxt[0]
        use_path = nxt[1]
        if visit[nxt_node] == False:
            visit[nxt_node] = True
            nxt_color += 1
            if nxt_color == color:
                nxt_color += 1
            dfs(nxt_node, nxt_color, use_path)
    
    nonlocal color_list
    if used_path != -1:
        color_list[used_path] = color

dfs(1, 0, -1)


for c in color_list:
    color_max = max(c, color_max)
print(color_max)
print(("\n".join(map(str, color_list))))

