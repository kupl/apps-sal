import queue
(H, W) = list(map(int, input().split()))
S = [0] * (H + 2)
S[0] = ''.join(['#'] * (W + 2))
S[-1] = ''.join(['#'] * (W + 2))
for i in range(1, H + 1):
    S[i] = '#' + input() + '#'
maxd = 0
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
for h in range(1, H + 1):
    for w in range(1, W + 1):
        if S[h][w] == '.':
            visited = [[False] * (W + 2) for _ in range(H + 2)]
            q = queue.Queue()
            visited[h][w] = True
            q.put([h, w, 0])
            while not q.empty():
                (a, b, c) = q.get()
                for i in range(4):
                    (y, x) = (a + dy[i], b + dx[i])
                    if S[y][x] == '.' and visited[y][x] == False:
                        q.put([y, x, c + 1])
                        visited[y][x] = True
            maxd = max(maxd, c)
print(maxd)
