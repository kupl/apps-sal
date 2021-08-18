h, w = map(int, input().split())
l = [input() for _ in range(h)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(h):
    for j in range(w):
        if l[i][j] == '#':
            cnt = 0
            for di in range(4):
                y = i + dx[di]
                x = j + dy[di]
                if x < 0 or y < 0 or x > w - 1 or y > h - 1:
                    continue
                else:
                    if l[y][x] == '#':
                        cnt += 1
            if cnt == 0:
                print('No')
                return

print('Yes')
