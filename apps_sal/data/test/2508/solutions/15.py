#!/usr/bin/env python3
from collections import deque


def main():
    H, W, K = map(int, input().split())
    x1, y1, x2, y2 = map(lambda x: int(x) - 1, input().split())
    c = [input() for _ in range(H)]

    adj = [[] for _ in range(W * H)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    INF = 10**12

    for i in range(H):
        for j in range(W):
            if c[i][j] == '@': continue
            for k in range(4):
                y = i + dy[k]
                x = j + dx[k]
                if 0 <= y < H and 0 <= x < W and c[y][x] == '.':
                    adj[W * i + j].append(W * y + x)

    queue = deque([W * x1 + y1])
    visit = [INF] * (W * H)
    visit[W * x1 + y1] = 0

    while queue:
        now = queue.popleft()
        for u in adj[now]:
            # nowからuの方向に'.'が続くかぎり（最大K個）
            count = 0
            direct = u - now
            fromC = now
            toC = u
            while count < K and toC in adj[fromC] and visit[now] < visit[toC]:
                count += 1
                if visit[toC] == INF:
                    queue.append(toC)
                    visit[toC] = visit[now] + 1
                fromC = toC
                toC += direct

    print(visit[W * x2 + y2]) if visit[W * x2 + y2] < INF else print(-1)
    # print(visit)


def __starting_point():
    main()


__starting_point()
