from copy import deepcopy
from collections import Counter, defaultdict, deque
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]


def maze_solve(S_1, S_2, maze_list):
    d = deque()
    dist[S_1][S_2] = 0
    d.append([S_1, S_2])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while d:
        v = d.popleft()
        x = v[0]
        y = v[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                d.append([nx, ny])
    return max(list(map(lambda x: max(x), dist)))


h, w = MI()
ans = 0
maze = [list(input()) for _ in range(h)]
dist = [[-1] * w for _ in range(h)]
start_list = []
for i in range(h):
    for j in range(w):
        if maze[i][j] == "
        dist[i][j] = 0
        else:
            start_list.append([i, j])
dist_copy = deepcopy(dist)
for k in start_list:
    dist = deepcopy(dist_copy)
    ans = max(ans, maze_solve(k[0], k[1], maze))
print(ans)
