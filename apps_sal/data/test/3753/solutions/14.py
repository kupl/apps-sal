import sys
input = sys.stdin.readline
n, m = [int(item) for item in input().split()]
field = []
field.append("#" * (m + 2))
for i in range(n):
    field.append("#" + input().rstrip() + "#")
field.append("#" * (m + 2))
visited = [[False] * (m + 2) for _ in range(n + 2)]
for i in range(2):
    q = [(1, 1)]
    while q:
        x, y = q.pop()
        if visited[x][y]:
            continue
        visited[x][y] = True
        if field[x + 1][y] != "#" and not visited[x + 1][y]:
            q.append((x + 1, y))
        if field[x][y + 1] != "#" and not visited[x][y + 1]:
            q.append((x, y + 1))
        if x == n and y == m:
            break
    if x != n or y != m:
        print(i)
        return
    visited[1][1] = False
    visited[n][m] = False
print(2)
