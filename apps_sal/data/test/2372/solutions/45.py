def main():
    (H, W) = list(map(int, input().split()))
    (y, x) = list(map(int, input().split()))
    start = (x + 1, y + 1)
    (y, x) = list(map(int, input().split()))
    goal = (x + 1, y + 1)
    dist_table = [[-2] * (W + 4)]
    dist_table.append([-2] * (W + 4))
    for _ in range(H):
        row = '##' + input() + '##'
        row = [-1 if c == '.' else -2 for c in row]
        dist_table.append(row)
    dist_table.append([-2] * (W + 4))
    dist_table.append([-2] * (W + 4))
    (sx, sy) = start
    dist_table[sy][sx] = 0
    move1 = ((-1, 0), (1, 0), (0, 1), (0, -1))
    move2 = ((-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2), (-1, -2), (-1, -1), (-1, 1), (-1, 2), (0, -2), (0, 2), (1, -2), (1, -1), (1, 1), (1, 2), (2, -2), (2, -1), (2, 0), (2, 1), (2, 2))
    queue1 = [start]
    queue2 = []
    while queue1:
        (now_x, now_y) = queue1.pop()
        if (now_x, now_y) == goal:
            break
        queue2.append((now_x, now_y))
        dist = dist_table[now_y][now_x]
        for (dx, dy) in move1:
            (tx, ty) = (now_x + dx, now_y + dy)
            if dist_table[ty][tx] == -1:
                dist_table[ty][tx] = dist
                queue1.append((tx, ty))
        if len(queue1) == 0:
            while queue2:
                (now_x, now_y) = queue2.pop()
                dist = dist_table[now_y][now_x]
                for (dx, dy) in move2:
                    (tx, ty) = (now_x + dx, now_y + dy)
                    if dist_table[ty][tx] == -1:
                        dist_table[ty][tx] = dist + 1
                        queue1.append((tx, ty))
    (gx, gy) = goal
    print(dist_table[gy][gx])


def __starting_point():
    main()


__starting_point()
