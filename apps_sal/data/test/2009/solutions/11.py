n = int(input())
r1, c1 = map(int, input().split())
r1, c1 = r1 - 1, c1 - 1
r2, c2 = map(int, input().split())
r2, c2 = r2 - 1, c2 - 1
T = [[] for i in range(n)]
for i in range(n):
    a = list(input())
    T[i] = a

k = 0
G = [[] for i in range(n * n)]
for i in range(n):
    for j in range(n):
        if T[i][j] == '0':
            que = [(i, j, k)]
            while que:
                x, y, d = que.pop()
                G[d].append((x, y))
                T[x][y] = '1'
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and T[nx][ny] == '0':
                        T[nx][ny] = '1'
                        que.append((nx, ny, d))
            k += 1

s = -1
e = -1
for k in range(n * n):
    if (r1, c1) in G[k]:
        s = k
    if (r2, c2) in G[k]:
        e = k

num = float('inf')
for sx, sy in G[s]:
    for ex, ey in G[e]:
        num = min(num, abs(sx - ex) ** 2 + abs(sy - ey) ** 2)

print(num)
