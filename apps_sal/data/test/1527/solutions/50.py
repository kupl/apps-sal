from collections import deque
H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

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
            for dh, dw in direction:
                if not ((0 <= nh + dh < H) and (0 <= nw + dw < W)):
                    continue
                if maze[nh + dh][nw + dw] == "
                continue
                if dist[nh + dh][nw + dw] != -1:
                    continue

                dist[nh + dh][nw + dw] = dist[nh][nw] + 1
                que.appendleft([nh + dh, nw + dw])

        ans = max(ans, max([max(d) for d in dist]))

print(ans)
