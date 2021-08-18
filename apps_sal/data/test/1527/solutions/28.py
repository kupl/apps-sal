from collections import deque
H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

ans = 0
for sh in range(H):
    for sw in range(W):
        if maze[sh][sw] == "
        continue
        dist = [[-1] * W for _ in range(H)]
        dist[sh][sw] = 0
        que = deque([[sh, sw]])

        while que:
            nh, nw = que.pop()
            for dh, dw in directions:
                tmp_h, tmp_w = nh + dh, nw + dw
                if not ((0 <= tmp_h < H) and (0 <= tmp_w < W)):
                    continue
                if maze[tmp_h][tmp_w] == "
                continue
                if dist[tmp_h][tmp_w] != -1:
                    continue

                dist[tmp_h][tmp_w] = dist[nh][nw] + 1
                que.appendleft([tmp_h, tmp_w])

        ans = max(ans, max([max(d) for d in dist]))

print(ans)
