from collections import deque


def main():
    h, w = map(int, input().split())
    c1, c2 = map(lambda x: int(x) + 1, input().split())
    d1, d2 = map(lambda x: int(x) + 1, input().split())
    work1 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    work2 = [(i, j) for i in range(-2, 3) for j in range(-2, 3) if (i, j) not in [(0, 0)] + work1]
    memo = ["
    dist = [[-1] * (w + 4) for _ in range(h + 4)]
    for i in range(h + 4):
        for j in range(w + 4):
            if memo[i][j] == "
                dist[i][j] = float("inf")
    que1 = deque([(c1, c2)])
    que2 = deque([])
    dist[c1][c2] = 0
    while que1:
        y, x = que1.popleft()
        score = dist[y][x]
        que2.append((y, x))
        for py, px in work1:
            ny, nx = y + py, x + px
            if dist[ny][nx] == -1:
                dist[ny][nx] = score
                que1.append((ny, nx))
        if not que1:
            while que2:
                y, x = que2.popleft()
                for py, px in work2:
                    ny, nx = y + py, x + px
                    if dist[ny][nx] == -1:
                        dist[ny][nx] = score + 1
                        que1.append((ny, nx))
    print(dist[d1][d2])


def __starting_point():
    main()


__starting_point()
