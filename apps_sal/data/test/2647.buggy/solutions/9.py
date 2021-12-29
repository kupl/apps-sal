def __starting_point():
    from collections import deque
    (H, W) = map(int, input().split())
    s = []
    black = 0
    for _ in range(H):
        t = list(input())
        for c in t:
            if c == '#':
                black += 1
        s.append(t)
    q = deque([(0, 0, 1)])
    s[0][0] = '#'
    while q:
        (x, y, d) = q.popleft()
        if x == H - 1 and y == W - 1:
            print(H * W - d - black)
            return
        for (nx, ny) in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            if 0 <= nx < H and 0 <= ny < W and (s[nx][ny] == '.'):
                s[nx][ny] = '#'
                q.append((nx, ny, d + 1))
    print(-1)


__starting_point()
