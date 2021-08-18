def main():
    from collections import deque

    H, W = list(map(int, input().split()))
    S = []
    num_path = 0
    for _ in range(H):
        s = input()
        num_path += s.count('.')
        S.append(s)

    move = ((0, 1), (0, -1), (1, 0), (-1, 0))
    distance = [[1] * W for _ in range(H)]
    queue = deque([(0, 0)])
    while queue:
        y, x = queue.popleft()
        if y == H - 1 and x == W - 1:
            break
        for dy, dx in move:
            ny = y + dy
            nx = x + dx
            if (1 and
                    0 <= ny < H and
                    0 <= nx < W and
                    distance[ny][nx] == 1 and
                    S[ny][nx] == '.'):
                queue.append((ny, nx))
                distance[ny][nx] = distance[y][x] + 1
    if distance[H - 1][W - 1] == 1:
        print((-1))
    else:
        print((num_path - distance[H - 1][W - 1]))


def __starting_point():
    main()


__starting_point()
