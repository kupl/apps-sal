dx = [1, 0, -1, 0, 1, -1, -1, 1]
dy = [0, 1, 0, -1, 1, 1, -1, -1]
(H, W) = map(int, input().split())
S = [input() for _ in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j] != '.':
            continue
        counter = 0
        for d in range(8):
            ni = i + dx[d]
            nj = j + dy[d]
            if ni < 0 or ni >= H or nj < 0 or (nj >= W):
                continue
            if S[ni][nj] == '#':
                counter += 1
        S[i] = S[i].replace('.', str(counter), 1)
for row in S:
    print(row)
