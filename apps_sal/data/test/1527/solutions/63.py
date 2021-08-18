from collections import deque
H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]
dist = [[-1] * W for _ in range(H)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
mx = 0
for h in range(H):
    for w in range(W):
        if field[h][w] == "
        continue
        dist = [[-1] * W for _ in range(H)]
        dist[h][w] = 0
        que = deque([])
        que.append([h, w])
        while que != deque([]):
            u, v = que.popleft()
            for dir in range(4):
                nu = u + dx[dir]
                nv = v + dy[dir]

                if (nu < 0) or (nu >= H) or (nv < 0) or (nv >= W):
                    continue
                if field[nu][nv] == "
                continue
                if dist[nu][nv] != -1:
                    continue

                que.append([nu, nv])
                dist[nu][nv] = dist[u][v] + 1

        for i in range(H):
            for j in range(W):
                if mx < dist[i][j]:
                    mx = dist[i][j]

print(mx)
