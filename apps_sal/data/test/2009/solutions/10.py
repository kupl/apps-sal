from collections import deque
n = int(input())

r1, c1 = (int(t)-1 for t in input().split(' '))
r2, c2 = (int(t)-1 for t in input().split(' '))

mx = [input() for _ in range(n)]

visited = [[0] * n for _ in range(n)]

def bfs(start, mark):
    q = deque()
    q.append(start)


    while len(q):
        r, c = q.popleft()
        if visited[r][c]: continue
        visited[r][c] = mark

        dirs = [(t[0] + r, t[1] + c) for t in [(0, 1), (1, 0), (-1, 0), (0, -1)] if t[0] + r < n and t[0] + r >= 0 and t[1] + c < n and t[1] + c >= 0]

        dirs = [d for d in dirs if not visited[d[0]][d[1]] and mx[d[0]][d[1]] == '0']
        for d in dirs:
            q.append(d)

bfs((r1, c1), 1)
if visited[r2][c2] == 1:
    print(0)
else:
    bfs((r2, c2), 2)
    firsts = [(i, j) for i in range(n) for j in range(n) if visited[i][j] == 1]
    seconds = [(i, j) for i in range(n) for j in range(n) if visited[i][j] == 2]
    result = min((f[0] - s[0])**2 + (f[1] - s[1])**2 for f in firsts for s in seconds)
    print(result)

