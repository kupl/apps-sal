(h, w) = map(int, input().split())
s = [list(input()) for i in range(h)]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
result = [[0] * w for _ in range(h)]
for y in range(h):
    for x in range(w):
        if s[y][x] == '#':
            result[y][x] = '#'
            continue
        count = 0
        for i in range(8):
            x_round = x + dx[i]
            y_round = y + dy[i]
            if x_round < 0 or w <= x_round or y_round < 0 or (h <= y_round):
                continue
            if s[y_round][x_round] == '#':
                count += 1
        result[y][x] = count
for y in range(h):
    for x in range(w):
        print(result[y][x], end='')
    print('')
