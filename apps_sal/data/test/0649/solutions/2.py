dr = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

n = int(input())
t = [int(i) for i in input().split()]
visited = set()
N = 150*2 + 10
covers = [[0]*N for i in range(N)]

def dfs(d, pos, path):
    mem = (d, pos, path)
    if mem in visited:
        return set()
    else:
        visited.add(mem)
    if d == n+1:
        return
    for _ in range(t[d-1]):
        pos = (pos[0] + dr[path][0], pos[1] + dr[path][1])
        covers[pos[0]][pos[1]] = 1
    dfs(d+1, pos, (path+1) % 8)
    dfs(d+1, pos, (path-1) % 8)

dfs(1, (int(N/2), int(N/2)), 0)
print(sum([sum(i) for i in covers]))

