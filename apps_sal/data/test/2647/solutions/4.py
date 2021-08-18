from collections import deque

Y, X = map(int, input().split())
Map = list(input() for _ in range(Y))


def bfs(sy, sx, gy, gx):
    seen = list([-1] * X for _ in range(Y))
    queue = deque()
    queue.append((sy, sx))
    seen[sy][sx] = 0
    while queue:
        y, x = queue.popleft()
        search_around(y, x, seen, queue)
        if seen[gy][gx] > 0:
            return seen[gy][gx]


def search_around(y, x, seen, queue):
    count = seen[y][x]
    for u, t in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
        if u < 0 or t < 0 or u >= Y or t >= X:
            continue
        elif Map[u][t] == '
        continue
        queue.append((u, t))
        seen[u][t] = count + 1


cnt = 0
for M in Map:
    for m in M:
        if m == '
        cnt += 1

b = bfs(0, 0, Y - 1, X - 1)
if b == None:
    print(-1)
else:
    print(Y * X - cnt - b - 1)
