h, w = list(map(int, input().split()))
field = [list(input()) for _ in range(h)]
dx = [1, 0, -1, 0, 1, -1, -1, 1]
dy = [0, 1, 0, -1, 1, 1, -1, -1]
for i in range(h):
    for j in range(w):
        if field[i][j] == "#":
            continue
        num = 0
        for k in range(8):
            ni = i + dy[k]
            nj = j + dx[k]
            if ni < 0 or h <= ni:
                continue
            if nj < 0 or w <= nj:
                continue
            if field[ni][nj] == "#":
                num += 1
        field[i][j] = str(num)
for out in field:
    print(("".join(out)))
