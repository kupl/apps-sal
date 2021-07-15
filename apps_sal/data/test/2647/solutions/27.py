def abc088d_grid_repainting():
    import heapq
    h, w = map(int, input().split())
    maze = []
    cnt = h * w
    for _ in range(h):
        s = input()
        maze.append(s)
        cnt -= s.count('#')
    q = [(1, 0, 0)]
    heapq.heapify(q)
    check = [[False] * w for _ in range(h)]
    while len(q) != 0:
        dis, x, y = heapq.heappop(q)
        if (x, y) == (h - 1, w - 1):
            print(cnt - dis)
            return
        for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            if 0 <= x + dx < h and 0 <= y + dy < w and maze[x + dx][y + dy] != '#' and not check[x + dx][y + dy]:
                check[x + dx][y + dy] = True
                heapq.heappush(q, (dis+1, x + dx, y + dy))
    print('-1')
abc088d_grid_repainting()
