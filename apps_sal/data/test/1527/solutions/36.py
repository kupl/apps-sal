from collections import deque

H, W = [int(x) for x in input().split()]

field = []
for i in range(H):
    field.append(input())

conn = [[[] for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if field[i][j] == '.':
            for e in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                h, w = i + e[0], j + e[1]
                if 0 <= h < H and 0 <= w < W and field[h][w] == '.':
                    conn[i][j].append([h, w])
d = 0
for i in range(H):
    for j in range(W):
        l = 0
        q = deque([[i, j]])
        dist = [[-1 for _ in range(W)] for _ in range(H)]
        dist[i][j] = 0
        while q:
            v = q.popleft()
            for w in conn[v[0]][v[1]]:
                if dist[w[0]][w[1]] == -1:
                    q.append(w)
                    dist[w[0]][w[1]] = dist[v[0]][v[1]] + 1
                    l = dist[w[0]][w[1]]

        d = max(d, l)

print(d)
