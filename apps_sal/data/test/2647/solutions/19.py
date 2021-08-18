H, W = map(int, input().split())
MAP = [list(input()) for _ in range(H)]
cnt = 0
for l in MAP:
    cnt += l.count("
FLAG=[[-1] * W for _ in range(H)]
FLAG[0][0]=1
q=[(0, 0)]
d=[(1, 0), (0, 1), (-1, 0), (0, -1)]

while q:
    y, x=q.pop(0)
    for dy, dx in d:
        if 0 <= y + dy < H and 0 <= x + dx < W and FLAG[y + dy][x + dx] == -1 and MAP[y + dy][x + dx] == ".":
            FLAG[y + dy][x + dx]=FLAG[y][x] + 1
            q.append((y + dy, x + dx))

if FLAG[H - 1][W - 1] == -1:
    print(-1)
else:
    print(H * W - FLAG[H - 1][W - 1] - cnt)
