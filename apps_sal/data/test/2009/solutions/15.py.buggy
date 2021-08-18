from collections import deque
from heapq import heappush, heappop
N = int(input())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
square = ["2" * (N + 2)] + ["2" + input() + "2" for _ in [0] * N] + ["2" * (N + 2)]


def bfs(startx, starty, v, goal=None):

    if v == 1:
        visited = [[0] * (N + 2) for _ in [0] * (N + 2)]
        visited[starty][startx] = 1
        s = set()
        add = s.add
        dq = deque([(startx, starty)])
        append, popleft = dq.append, dq.popleft

        while dq:
            x, y = popleft()
            add((x, y))
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if square[ny][nx] == "0" and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    append((nx, ny))

        return s
    else:
        visited = [[10**9] * (N + 2) for _ in [0] * (N + 2)]
        visited[starty][startx] = 0
        heap = [(0, startx, starty)]
        while heap:
            cost, x, y = heappop(heap)
            if (x, y) in goal:
                return (x, y)
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                new_cost = abs(nx - startx)**2 + abs(ny - starty)**2
                if square[ny][nx] != "2" and visited[ny][nx] > new_cost:
                    visited[ny][nx] = new_cost
                    heappush(heap, (new_cost, nx, ny))

        return (10**9, 10**9)


s1 = bfs(sx, sy, 1)
s2 = bfs(gx, gy, 1)
if s1 == s2:
    print(0)
    return

ans = 10**9
for x, y in s1:
    for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if square[ny][nx] == "1":
            destx, desty = bfs(nx, ny, 2, s2)
            dist = abs(x - destx)**2 + abs(y - desty)**2
            if ans > dist:
                ans = dist

print(ans)
