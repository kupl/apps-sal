(h, w) = map(int, input().split())
l = [input() for _ in range(h)]
k = [['#' for x in range(w)] for _ in range(h)]
dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
for i in range(h):
    for j in range(w):
        if l[i][j] == '.':
            cnt = 0
            for di in range(8):
                x = j + dx[di]
                y = i + dy[di]
                if x < 0 or y < 0 or x >= w or (y >= h):
                    continue
                if l[y][x] == '#':
                    cnt += 1
            k[i][j] = cnt
for i in range(h):
    print(''.join(map(str, k[i])))
