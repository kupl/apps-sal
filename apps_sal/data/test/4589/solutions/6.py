def resolve():
    (h, w) = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(list(input()))
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    for x in range(h):
        for y in range(w):
            if s[x][y] == '#':
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if not (nx < h and 0 <= nx and (ny < w) and (0 <= ny)) or s[nx][ny] == '#':
                        continue
                    if s[nx][ny] == '.':
                        s[nx][ny] = '1'
                    else:
                        s[nx][ny] = str(ord(s[nx][ny]) - ord('0') + 1)
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                s[i][j] = '0'
    for i in range(h):
        print(''.join(s[i]))


resolve()
