from collections import deque

H, W = [int(x) for x in input().split()]
board = []
for _ in range(H):
    board.append(input())

white = sum([board[h].count('.') for h in range(H)])

dist = {(x, y): white + 1 for x in range(W) for y in range(H)}
q = deque([(0, 0)])
dist[(0, 0)] = 1
while q:
    x, y = q.popleft()
    for d in range(4):
        nx, ny = x + int(((1j)**d).real), y + int(((1j)**d).imag)
        if nx < 0 or W <= nx or ny < 0 or H <= ny:
            continue
        if board[ny][nx] == '#':
            continue
        if dist[(nx, ny)] <= white:
            continue
        dist[(nx, ny)] = dist[(x, y)] + 1
        q.append((nx, ny))

lenofpath = dist[(W - 1, H - 1)]
ans = white - lenofpath
print(ans)
