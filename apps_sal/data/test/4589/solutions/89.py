(h, w) = map(int, input().split())
m = [input() for _ in range(h)]
vx = [0, 1, 1, 1, 0, -1, -1, -1]
vy = [1, 1, 0, -1, -1, -1, 0, 1]
ans = [['#'] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if m[i][j] == '#':
            ans[i][j] = '#'
            continue
        count = 0
        for k in range(8):
            ny = vy[k] + i
            nx = vx[k] + j
            if 0 <= ny and ny < h and (0 <= nx) and (nx < w):
                if m[ny][nx] == '#':
                    count += 1
        ans[i][j] = str(count)
for i in ans:
    print(''.join(i))
