(n, m) = list(map(int, input().split()))
data = [list(map(int, input().split())) for i in range(m)]


def dfs(pos):
    if visit[pos] == 1:
        return
    visit[pos] = 1
    for i in range(n):
        if graph[pos][i] == 1:
            dfs(i)


count = 0
for hen in range(m):
    graph = [[0] * n for i in range(n)]
    visit = [0] * n
    for i in range(m):
        pos1 = data[i][0] - 1
        pos2 = data[i][1] - 1
        if i != hen:
            graph[pos1][pos2] = 1
            graph[pos2][pos1] = 1
    dfs(0)
    connected = True
    for i in range(n):
        if visit[i] == 0:
            connected = False
    if not connected:
        count += 1
print(count)
