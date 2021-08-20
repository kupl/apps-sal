from collections import deque
(H, W) = map(int, input().split())
M = []
M = ['#' * (W + 2)]
num_blk = 0
for h in range(H):
    inp = input()
    M.append('#' + inp + '#')
    num_blk += inp.count('#')
M.append('#' * (W + 2))
(sy, sx) = (1, 1)
(gy, gx) = (H, W)
T = [[float('inf')] * (W + 2) for _ in range(H + 2)]
T[sy][sx] = 0
que = deque([(sy, sx)])
while len(que) > 0:
    (y, x) = que.popleft()
    for (a, b) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if M[y + b][x + a] != '#' and T[y + b][x + a] == float('inf'):
            T[y + b][x + a] = T[y][x] + 1
            que.append((y + b, x + a))
    if y == gy and x == gx:
        break
if T[gy][gx] == float('inf'):
    print(-1)
else:
    print(H * W - num_blk - T[gy][gx] - 1)
