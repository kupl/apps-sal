import sys
input = sys.stdin.readline
sys.setrecursionlimit(99999)

n = int(input())
x, y = map(int, input().split())
r, c = map(int, input().split())
adj = [list(map(int, input().rstrip()))for _ in range(n)]

dx = [0, 0, -1, 1]
dy = dx[::-1]
valid = lambda x, y: 0 <= x < n and 0 <= y < n
visit = [[False] * 51 for _ in range(51)]


def dfs(x, y, ans):
    if visit[x][y]: return
    visit[x][y] = True
    ans.append((x, y))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not valid(nx, ny): continue
        if adj[nx][ny]: continue
        dfs(nx, ny, ans)


start = []; end = []
dfs(x - 1, y - 1, start)
if (r - 1, c - 1) in start:
    print(0)
    return
dfs(r - 1, c - 1, end)


ans = 10**100
for x, y in start:
    for a, b in end:
        ans = min(ans, (a - x)**2 + (y - b)**2)
print(ans)
