import queue
connect = [[0 for i in range(401)] for j in range(401)]


def bfs(val):
    q = queue.Queue()
    dis = [-1 for i in range(401)]
    dis[1] = 0
    q.put(1)
    while not q.empty():
        x = q.get()
        for i in range(1, n + 1):
            if connect[x][i] == val and dis[i] == -1:
                dis[i] = dis[x] + 1
                q.put(i)
    return dis[n]


temp = input().split()
n = int(temp[0])
m = int(temp[1])
dis = [[[0 for i in range(401)] for j in range(401)] for k in range(2)]
for i in range(m):
    temp = input().split()
    u = int(temp[0])
    v = int(temp[1])
    connect[u][v] = connect[v][u] = 1
print(bfs(1 - connect[1][n]))
