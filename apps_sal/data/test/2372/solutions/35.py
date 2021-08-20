from collections import deque


def solve(H, W, Ch, Cw, Dh, Dw, maze):
    walled_maze = ['##{}##'.format(row) for row in maze]
    walled_maze.insert(0, '##{}##'.format('#' * W))
    walled_maze.insert(0, '##{}##'.format('#' * W))
    walled_maze.append('##{}##'.format('#' * W))
    walled_maze.append('##{}##'.format('#' * W))
    INF = 10 ** 12
    path = [[INF] * (W + 4) for _ in range(H + 4)]
    walk = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    warp = [(i, j) for i in range(-2, 3) for j in range(-2, 3) if (i, j) not in [(0, 0)] + walk]
    yet = deque()
    yet.append((Ch + 2, Cw + 2, 0))
    path[Ch + 2][Cw + 2] = 0
    done = deque()
    while yet:
        (y, x, s) = yet.popleft()
        done.append((y, x, s))
        for (dy, dx) in walk:
            ny = y + dy
            nx = x + dx
            if walled_maze[ny][nx] == '.' and path[ny][nx] > s:
                path[ny][nx] = s
                yet.append((ny, nx, s))
        if len(yet) == 0:
            while done:
                (y, x, s) = done.popleft()
                for (dy, dx) in warp:
                    ny = y + dy
                    nx = x + dx
                    if walled_maze[ny][nx] == '.' and path[ny][nx] > s + 1:
                        path[ny][nx] = s + 1
                        yet.append((ny, nx, s + 1))
    ans = path[Dh + 2][Dw + 2] if path[Dh + 2][Dw + 2] < INF else -1
    print(ans)


def __starting_point():
    (H, W) = list(map(int, input().split()))
    (Ch, Cw) = [int(x) - 1 for x in input().split()]
    (Dh, Dw) = [int(x) - 1 for x in input().split()]
    maze = [input() for _ in range(H)]
    solve(H, W, Ch, Cw, Dh, Dw, maze)


__starting_point()
