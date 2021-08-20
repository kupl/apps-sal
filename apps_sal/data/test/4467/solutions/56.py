n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(n)]
g = [[0 for _ in range(2 * n + 2)] for _ in range(2 * n + 2)]
for (i, (a, b)) in enumerate(ab):
    fr = i + 2
    g[0][fr] = 1
    for (j, (c, d)) in enumerate(cd):
        to = n + j + 2
        g[to][1] = 1
        if a < c and b < d:
            g[fr][to] = 1
used = [False for _ in range(2 * n + 2)]
path = []
goal = 1
flow = [[0 for _ in range(2 * n + 2)] for _ in range(2 * n + 2)]


def bfs(v):
    used[v] = True
    for next in range(2 * n + 2):
        if g[v][next] == 0 or used[next]:
            pass
        elif next == goal:
            path.append(v)
            return True
        elif bfs(next):
            path.append(v)
            return True
    return False


ans = 0
while bfs(0):
    path.reverse()
    path.append(1)
    for i in range(len(path) - 1):
        g[path[i]][path[i + 1]] -= 1
        g[path[i + 1]][path[i]] += 1
    used = [False for _ in range(2 * n + 2)]
    path = []
    ans += 1
print(ans)
