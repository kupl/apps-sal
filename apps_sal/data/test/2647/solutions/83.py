def cal():
    import queue
    h, w = list(map(int, input().split()))
    s = [list(input()) for _ in range(h)]
    cost = [[-1] * w for _ in range(h)]
    INF = float('inf')
    count, ans = 0, INF
    for i in range(h):
        for j in range(w):
            if s[i][j] != '
            cost[i][j] = INF
            else:
                count += 1
    q = queue.Queue()
    q.put((0, 0, 1))
    while not q.empty():
        c0, c1, c2 = q.get()
        s[c0][c1] = '
        if c0 == h - 1 and c1 == w - 1:
            return h * w - count - c2
        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x, y = c0 + i, c1 + j
            if 0 <= x < h and 0 <= y < w:
                if s[x][y] != '
                cost[x][y] = c2 + 1
                q.put((x, y, c2 + 1))

    return ans


ans = cal()
if ans == float('inf'):
    print((-1))
else:
    print(ans)
