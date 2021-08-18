def main():
    import sys
    from collections import deque
    input = sys.stdin.readline

    h, w, k = list(map(int, input().split()))
    sy, sx, gy, gx = list(map(int, input().split()))

    maze = [tuple(input()) for _ in range(h)]

    sy -= 1
    sx -= 1
    gy -= 1
    gx -= 1

    dis = [[-1] * w for _ in range(h)]

    dis[sy][sx] = 0

    d = deque([(sx, sy)])
    while len(d) > 0:
        (x, y) = d.popleft()
        if x == gx and y == gy:
            print((dis[gy][gx]))

            return

        for (mx, my) in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            for j in range(1, k + 1):
                nx = x + mx * j
                ny = y + my * j
                if 0 <= nx < w and 0 <= ny < h:
                    if maze[ny][nx] == "." and (dis[ny][nx] == -1 or dis[ny][nx] == dis[y][x] + 1):
                        if dis[ny][nx] == -1:
                            d.append((nx, ny))
                        dis[ny][nx] = dis[y][x] + 1

                    else:
                        break
                else:
                    break

    print((-1))


def __starting_point():
    main()


__starting_point()
