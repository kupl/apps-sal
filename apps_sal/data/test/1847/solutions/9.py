limit = 10**9
mark = set()
dist = {}
dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]

def calc(x, y):
    nonlocal limit
    val = x
    val = val * limit + y
    return val

def bfs():
    nonlocal x0, y0, x1, y1, mark, dist, dx, dy
    myqueue = []
    S = calc(x0, y0)
    myqueue.append(S)
    dist[S] = 0

    while myqueue:
        u = myqueue.pop(0)
        x = u // limit
        y = u % limit

        for i in range(8):
            xx = x + dx[i]
            yy = y + dy[i]
            v = calc(xx, yy)
            if (1 <= xx <= limit and 1 <= yy <= limit and v in mark):
                if v not in dist:
                    dist[v] = dist[u] + 1
                    if v == calc(x1, y1):
                        print(dist[v])
                        return
                    myqueue.append(v)

    print(-1)

x0, y0, x1, y1 = list(map(int, input().split()))
mark.add(calc(x0, y0))
mark.add(calc(x1, y1))

n = int(input())

for i in range(1, n+1):
    r, a, b = list(map(int, input().split()))
    for j in range(a, b+1):
        mark.add(calc(r, j))

bfs()

