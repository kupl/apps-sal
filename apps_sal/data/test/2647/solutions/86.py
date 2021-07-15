from collections import deque


def main():
    H, W = list(map(int, input().split()))
    field = [list(input().rstrip()) for _ in range(H)]

    black = 0

    for f in field:
        for s in f:
            if s == "#":
                black += 1

    dir_h = [0, 0, 1, -1]
    dir_w = [1, -1, 0, 0]

    print((H * W - black - bfs(H, W, field, dir_h, dir_w)))


def bfs(H, W, field, dir_h, dir_w):
    q = deque([])
    seen = [[-1 for _ in range(W)] for _ in range(H)]

    q.append([0, 0])
    seen[0][0] = 1

    while q:
        h, w = q.popleft()

        for dh, dw in zip(dir_h, dir_w):
            nh, nw = h + dh, w + dw

            if nh < 0 or nh >= H or nw < 0 or nw >= W:
                continue
            elif field[nh][nw] == "#":
                continue
            elif seen[nh][nw] != -1:
                continue

            seen[nh][nw] = seen[h][w] + 1
            q.append([nh, nw])

    if seen[H - 1][W - 1] == -1:
        print((-1))
        return

    return seen[H - 1][W - 1]


def __starting_point():
    main()

__starting_point()
